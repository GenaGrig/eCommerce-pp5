from django.shortcuts import render, redirect, reverse


def view_cart(request):
    '''A view to return the shopping cart page'''
    
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    '''Add a quantity of the specified product to the shopping cart'''

    # Get the quantity from the POST data
    quantity_str = request.POST.get('quantity')

    # Check if quantity_str is None or an empty string
    if quantity_str is None or not quantity_str.strip():
        # Handle the case where quantity is not provided
        # You might want to add some error handling or redirect to an error page
        return redirect(reverse('all_products'))

    # Convert the quantity to an integer
    quantity = int(quantity_str)

    cart = request.session.get('cart', {})

    if item_id in cart:
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(reverse('all_products'))

