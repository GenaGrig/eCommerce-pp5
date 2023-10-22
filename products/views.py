from django.shortcuts import render
from .models import Product


def all_products(request):
    ''' A view to show all products, including sorting and search queries '''

    products = Product.objects.all()
    quantity_in_stock = Product.objects.filter(quantity_in_stock__gt=0).count()

    context = {
        'products': products,
        'quantity_in_stock': quantity_in_stock,
    }

    return render(request, 'products/products.html', context)
