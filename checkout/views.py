from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    ''' A view to return the checkout page'''
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': "pk_test_51Nx9gOLYlzsmJrfJCgH8J3fqTfLdxucTrkvJziA4LmOizRa6PjujrurYXmBxqJaeIqeW5onytm9vpKYMVHzlJKDQ00aXPMQT7g",
        'client_secret': 'test client secret',
    }

    return render(request, template, context)