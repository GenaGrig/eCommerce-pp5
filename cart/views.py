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
            messages.info(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

        # Update the session with the new cart
        request.session['cart'] = cart

        # Redirect to the cart view
        return redirect('product_detail', product.id)
    
    except Exception as e:
        messages.error(request, f'Error adding item: {e}')
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
    messages.info(request, f'Updated {product.name} quantity to {cart[item_id]}')

    request.session['cart'] = cart

    return redirect('view_cart')


def remove_from_cart(request, item_id):
    '''Remove the item from the shopping cart'''
    
    try:
        product = get_object_or_404(Product, pk=item_id)

        cart = request.session.get('cart', {})

        if item_id in cart:
            del cart[item_id]
            messages.warning(request, f'Item {product.name} removed from your cart')

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))
    
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return redirect(reverse('view_cart'))
