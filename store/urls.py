from django.urls import path
from . import views
from products.views import all_products

urlpatterns = [
    path("", views.index, name="index"),
    path('products/', all_products, name='all_products')
]
