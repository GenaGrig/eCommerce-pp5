from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower


def all_products(request):
    ''' A view to show all products, including sorting and search queries '''

    products = Product.objects.all()
    quantity_in_stock = Product.objects.filter(quantity_in_stock__gt=0).count()
    query = None
    category = None
    sort = None
    direction = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q'].strip()  # Strip whitespace from the query
            if not query:  # Check if the query is empty after stripping whitespace
                messages.error(request, "You didn't enter any valid search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'price':
                sortkey = 'price'
            elif sortkey == 'rating':
                sortkey = 'rating'
            else:
                sortkey = 'name'  # Set a default sort field if 'sort' is not recognized

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'quantity_in_stock': quantity_in_stock,
        'search_term': query,
        "current_categories": category,
        'show_delivery_banner': True,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    ''' A view to show individual product details '''

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'show_delivery_banner': True,
    }

    return render(request, 'products/product_detail.html', context)


def get_descendant_categories(category):
    ''' Returns a list of all descendant categories of a given category'''
    descendants = [category]
    for child_category in category.category_set.all():
        descendants += get_descendant_categories(child_category)
    return descendants


def products_in_category(request, category_id):
    ''' A view to show products in a specific category'''
    category = get_object_or_404(Category, id=category_id)

    # Get all descendant categories (including the current category)
    descendant_categories = get_descendant_categories(category)

    # Retrieve products from the descendant categories
    products_in_category = Product.objects.filter(category__in=descendant_categories)
    
    context = {
        'category': category,
        'products': products_in_category,
        'show_delivery_banner': True,
    }

    return render(request, 'products/products_in_category.html', context)
