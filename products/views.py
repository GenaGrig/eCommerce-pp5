import logging
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Product, Category, Wishlist


def all_products(request):
    ''' A view to show all products, including sorting and search queries '''

    products = Product.objects.all()
    quantity_in_stock = Product.objects.filter(quantity_in_stock__gt=0).count()
    parent_categories = Category.objects.filter(parent_category_id__isnull=True)
    query = None
    categories = None
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
            elif sortkey == 'category':
                sortkey = 'category'
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
        "current_categories": parent_categories,
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
    
    # Sorting logic
    sort = request.GET.get('sort', 'name')
    direction = request.GET.get('direction', 'asc')

    if sort == 'name':
        sort_field = 'name'
    elif sort == 'price':
        sort_field = 'price'
    elif sort == 'rating':
        sort_field = 'rating'
    else:
        sort_field = 'name'

    if direction == 'desc':
        sort_field = f'-{sort_field}'

    products_in_category = products_in_category.order_by(sort_field)
    
    context = {
        'category': category,
        'products': products_in_category,
        'current_sorting': f'{sort}_{direction}',
        'show_delivery_banner': True,
    }

    return render(request, 'products/products_in_category.html', context)


def wishlist_test(request):
    ''' A view to show the wishlist '''
    wishlist_instance = Wishlist.objects.get(user=request.user)
    products = wishlist_instance.products.all()
    context = {
        'wishlist': wishlist_instance,
        'show_delivery_banner': True,
        'products': products,
    }
    return render(request, 'products/wishlist_test.html', context)


logger = logging.getLogger(__name__)


@login_required
def add_to_wishlist(request, product_id):
    ''' A view to add a product to the wishlist '''
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    
    # Log a message
    logger.info(f"Product '{product.name}' added to wishlist for user '{request.user}'")
    
    return redirect('wishlist_test')


@login_required
def remove_from_wishlist(request, product_id):
    ''' A view to remove a product from the wishlist '''
    product = Product.objects.get(id=product_id)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.products.remove(product)
    return redirect('wishlist_test')
    