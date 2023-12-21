from django.shortcuts import redirect


def index(request):
    '''A view to redirect from the index page to the products page'''

    return redirect('all_products')
