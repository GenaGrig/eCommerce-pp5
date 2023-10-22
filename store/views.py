from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    '''A view to redirect from the index page to the products page'''
    
    return redirect('all_products')
