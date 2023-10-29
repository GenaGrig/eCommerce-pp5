from decimal import Decimal, InvalidOperation
from django.utils import timezone
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from products.models import Product
from .models import Coupon


def view_cart(request):
    '''A view to return the shopping cart page'''

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    '''Add a quantity of the specified product to the shopping cart'''

    try:
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, pk=item_id)

        cart = request.session.get('cart', {})
        
        # Update the quantity in the cart dictionary
        if item_id in cart:
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

        # Update the session with the new cart
        request.session['cart'] = cart

        # Redirect to the cart view
        return redirect('view_cart')
    
    except Exception as e:
        # Handle any exceptions and return an error response if needed
        return redirect('view_cart')


@require_POST
def update_cart(request, item_id):
    '''Update the quantity of the specified product to the specified amount'''
    quantity = int(request.POST['quantity'])

    # Assuming you have a model named Product
    product = get_object_or_404(Product, pk=item_id)

    # Perform your logic to update the cart or session here
    # For simplicity, let's assume you're updating a session variable named 'cart'
    cart = request.session.get('cart', {})
    cart[item_id] = quantity
    request.session['cart'] = cart

    return redirect('view_cart')


def remove_from_cart(request, item_id):
    '''Remove the item from the shopping cart'''

    cart = request.session.get('cart', {})

    if item_id in cart:
        del cart[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def calculate_total_price(cart, request):
    total_price = 0
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total_price += Decimal(quantity) * product.price

    # If 'total' is available in the session, use it
    total_price = request.session.get('total', total_price)

    return total_price


def apply_coupon(request):
    if request.method == 'POST':
        coupon_code = request.POST.get('coupon_code')
        try:
            coupon = Coupon.objects.get(code=coupon_code, active=True)
            total_price = request.session.get('grand_total', 0)
            discount_percentage = float(coupon.discount_percentage)
            discount_amount = float(total_price) * float(discount_percentage / 100)

            request.session['coupon'] = {
                'code': coupon.code,
                'discount_percentage': discount_percentage,
                'discount_amount': discount_amount
            }

            messages.success(request, 'Coupon applied successfully!')
        except Coupon.DoesNotExist:
            messages.error(request, 'Invalid coupon code or coupon is inactive.')

    return redirect('view_cart')


def calculate_discount(grand_total, discount_percentage):
    '''Calculate the discount amount based on the grand total and discount percentage'''
    try:
        grand_total = Decimal(grand_total)
        discount_percentage = Decimal(discount_percentage)
    except InvalidOperation as e:
        # Handle the exception, e.g., log an error or return an appropriate default value
        return Decimal('0.00')

    discount_amount = grand_total * (discount_percentage / Decimal(100))
    return discount_amount


