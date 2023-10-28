from django.shortcuts import get_object_or_404
from products.models import Product
from django.conf import settings


def cart_contents(request):
    '''Ensures that the cart contents are available when rendering every page'''

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total + settings.STANDARD_DELIVERY_COST
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
        
    tax = total * 0.2
        
    grand_total = delivery + total

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'id': id,
            'quantity': quantity,
            'product': product,
        })

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

    return (context)
