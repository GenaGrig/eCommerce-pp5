from django.shortcuts import redirect, render


def index(request):
    '''A view to redirect from the index page to the products page'''

    return redirect('all_products')


def page_under_construction(request):
    '''A view to redirect from the index page to the products page'''

    return render(request, 'store/page-under-construction.html')
