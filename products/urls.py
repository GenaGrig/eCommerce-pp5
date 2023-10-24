from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_products, name="products"),
    path("<product_id>", views.product_detail, name="product_detail"),
    path("category/<category_id>", views.products_in_category, name="products_in_category"),
]
