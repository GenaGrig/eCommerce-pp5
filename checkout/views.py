from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

import stripe
import json

from profiles.models import UserProfile
from profiles.forms import UserProfileForm

from cart.contexts import cart_contents
from products.models import Product
from .forms import OrderForm
from .models import Order, OrderLineItem, Coupon


@require_POST
def cache_checkout_data(request):
    ''' A view to cache checkout data'''
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
            'order_id': request.POST.get('order_id'),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    ''' A view to return the checkout page'''

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email_address': request.POST['email_address'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postal_code': request.POST['postal_code'],
            'city': request.POST['city'],
            'street_address1': request.POST['street_address1'],
            'building_number1': request.POST['building_number1'],
            'street_address2': request.POST['street_address2'],
            'building_number2': request.POST['building_number2'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                        )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in \
                            our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_id]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart \
                at the moment")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            metadata={
                'cart': json.dumps(request.session.get('cart', {})),
                'username': request.user,
                'save_info': 'save-info' in request.POST,
                'order_id': 'order.id',
            }
        )

        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'first_name': user_profile.default_first_name,
                    'last_name': user_profile.default_last_name,
                    'email_address': user_profile.default_email_address,
                    'phone_number': user_profile.default_phone_number,
                    'country': user_profile.default_country,
                    'postal_code': user_profile.default_postal_code,
                    'city': user_profile.default_city,
                    'street_address1': user_profile.default_street_address1,
                    'building_number1': user_profile.default_building_number1,
                    'street_address2': user_profile.default_street_address2,
                    'building_number2': user_profile.default_building_number2,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_id):
    ''' A view to return the checkout success page'''

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_id=order_id)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_first_name': order.first_name,
                'default_last_name': order.last_name,
                'default_email_address': order.email_address,
                'default_phone_number': order.phone_number,
                'default_street_address1': order.street_address1,
                'default_building_number1': order.building_number1,
                'default_street_address2': order.street_address2,
                'default_building_number2': order.building_number2,
                'default_city': order.city,
                'default_postal_code': order.postal_code,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    tax_rate = settings.TAX_RATE
    tax = order.order_total * tax_rate / 100

    order.tax = tax
    order.save()

    messages.success(request, f'Order successfully processed! \
                Your order number is {order.order_id}. \
                A confirmation email will be sent to {order.email_address}.')

    if 'cart' in request.session:
        update_product_quantities(request)
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'save_info': save_info,
    }

    return render(request, template, context)


def update_product_quantities(request):
    ''' A view to update product quantities after a successful checkout'''

    cart = request.session.get('cart', {})
    for item_id, item_data in cart.items():
        try:
            product = Product.objects.get(id=item_id)
            product.quantity_in_stock -= item_data
            product.save()
        except Product.DoesNotExist:
            messages.error(request, (
                "One of the products in your bag wasn't found \
                    in our database. "
                "Please call us for assistance!")
            )
            return redirect(reverse('view_cart'))


def apply_coupon(request):
    ''' A view to apply a coupon to the order'''
    if request.method == 'POST':
        coupon_code = request.POST.get('coupon_code')
        if coupon_code:
            try:
                coupon = (Coupon.objects.get(coupon_code=coupon_code,
                                             active=True))
                # Implement this function to get or create the order
                order = get_or_create_order(request)
                # Implement a method in your Order model to apply the coupon
                order.apply_coupon(coupon)
                messages.success(request, f"Coupon '{coupon.coupon_code}'\
                                applied successfully! \
                                Coupon value is {coupon.coupon_value} eur.")
            except Coupon.DoesNotExist:
                messages.error(request, "Invalid coupon code.")

    return redirect(reverse('checkout'))


def get_or_create_order(request):
    ''' A view to get or create an order'''
    order_id = request.session.get('order_id')
    if order_id:
        order = Order.objects.get(id=order_id)
    else:
        order = Order.objects.create()
        request.session['order_id'] = order.id
    return order
