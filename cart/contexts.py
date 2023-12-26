from django.shortcuts import get_object_or_404
from products.models import Product
from django.conf import settings
from decimal import Decimal


def cart_contents(request):
    '''Ensures that the cart contents are available when rendering
    every page'''

    cart = request.session.get('cart', {})

    cart_items = []
    total = Decimal('0.00')
    product_count = 0

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += Decimal(quantity) * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_COST
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

    tax = total * settings.TAX_RATE / 100

    if total > 0:
        grand_total = float(total) + float(delivery)
    else:
        grand_total = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'tax': tax,
    }

    return context


def wishlist_contents(request):
    '''Ensures that the wishlist contents are available when
    rendering every page'''

    wishlist = request.session.get('wishlist', {})

    wishlist_items = []
    product_count_wishlist = 0

    for item_id, quantity in wishlist.items():
        product = get_object_or_404(Product, pk=item_id)
        product_count_wishlist += quantity
        wishlist_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'wishlist_items': wishlist_items,
        'product_count_wishlist': product_count_wishlist,
    }

    return context
