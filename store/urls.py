from django.urls import path
from products.views import all_products
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('products/', all_products, name='all_products'),
    path('page-under-construction/',
         views.page_under_construction,
         name='page_under_construction'),
]
