from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db import IntegrityError
from django.contrib import messages
from django.db.models import Q, Avg
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Product, Category, Wishlist, Subscriber, Review
from .forms import ProductForm


def all_products(request):
    ''' A view to show all products, including sorting and search queries '''

    products = Product.objects.all()
    quantity_in_stock = Product.objects.filter(quantity_in_stock__gt=0).count()
    parent_categories = Category.objects.\
        filter(parent_category_id__isnull=True)
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'q' in request.GET:
            # Strip whitespace from the query
            query = request.GET['q'].strip()
            # Check if the query is empty after stripping whitespace
            if not query:
                messages.error(request, "You didn't enter any valid \
                    search criteria!")
                return redirect(reverse('products'))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query))
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
                sortkey = 'name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    for product in products:
        average_rating = Review.objects.filter(product=product)\
            .aggregate(Avg('rating'))['rating__avg']
        product.rating = average_rating
        product.save()

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

    # Calculate the average rating for the product
    product.average_rating = Review.objects.filter(product=product)\
        .aggregate(Avg('rating'))['rating__avg']

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
    products_in_category = (Product.objects.filter
                            (category__in=descendant_categories))

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
    try:
        wishlist_items = Wishlist.objects.get(user=request.user)
        products = wishlist_items.products.all()
        date_added = wishlist_items.date_added
    except Wishlist.DoesNotExist:
        messages.info(request, "You don't have an active wishlist")
        wishlist = Wishlist.objects.create(user=request.user)
        wishlist.save()

    context = {
        'wishlist_items': wishlist_items,
        'show_delivery_banner': True,
        'products': products,
        'date_added': date_added,
    }

    return render(request, 'products/wishlist_test.html', context)


@login_required
def add_to_wishlist(request, product_id):
    ''' A view to add a product to the wishlist '''
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)

    print(wishlist.date_added)

    messages.warning(request, f'Added {product.name} to your wishlist')
    return redirect('products')


@login_required
def remove_from_wishlist(request, product_id):
    ''' A view to remove a product from the wishlist '''
    product = Product.objects.get(id=product_id)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.products.remove(product)

    messages.warning(request, f'Removed {product.name} from your wishlist')
    return redirect('wishlist_test')


@login_required
def add_product(request):
    ''' Add a product to the store '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('products'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Successfully added {product.name}!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure \
                the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    ''' Edit a product in the store '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('products'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    ''' Delete a product from the store '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('products'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} deleted!')
    return redirect(reverse('products'))


def subscribe_to_newsletter(request):
    ''' A view to subscribe to the mailing list '''
    if request.method == 'POST':
        email = request.POST.get('email')

        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
        else:
            messages.error(request, 'You are already subscribed to\
                our newsletter!')
            return redirect(reverse('products'))
    messages.success(request, 'You have successfully subscribed to\
        our newsletter!')
    return render(request, 'products/subscribe.html')


def unsubscribe_from_newsletter(request):
    ''' A view to unsubscribe from the mailing list '''
    if request.method == 'POST':
        # Check if the user is authenticated
        if request.user.is_authenticated:
            email = request.user.email
            print(f"Authenticated user's email: {email}")
        else:
            # If the user is not authenticated, try to get the email
            # from the POST data
            email = request.POST.get('email')

        # Check if the email exists in the Subscriber model
        if Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber.objects.get(email=email)
            subscriber.delete()
            messages.success(request, 'You have successfully unsubscribed from\
                our newsletter!')
        else:
            messages.error(request, 'You are not subscribed to \
                our newsletter!')

        # Redirect to a relevant page (e.g., 'products' page)
        return redirect(reverse('products'))

    return render(request, 'products/unsubscribe.html')


def page_not_found(request):
    ''' A view to handle 404 errors '''
    return render(request, '404.html', status=404)


@login_required
def submit_review(request, product_id):
    ''' A view to submit a rating for a product '''
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        try:
            # Attempt to create a new rating
            Review.objects.create(
                user=request.user,
                product=product,
                rating=rating)
            messages.success(request, 'Your rating value has been submitted\
                successfully.')
        except IntegrityError:
            # Handle the case where a rating already exists for the user
            # and product
            messages.error(request, 'You have already rated for this product.')

        return redirect(reverse('product_detail', args=[product.id]))
    return render(request, 'products/product_detail.html',
                  {'product': product})
