from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    ''' A view to show individual product details '''

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)