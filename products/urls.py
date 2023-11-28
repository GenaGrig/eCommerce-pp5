from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.all_products, name="products"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    path("category/<category_id>", views.products_in_category, name="products_in_category"),
    path("wishlist_test/", views.wishlist_test, name="wishlist_test"),
    path("add_to_wishlist/<product_id>", views.add_to_wishlist, name="add_to_wishlist"),
    path("remove_from_wishlist/<product_id>", views.remove_from_wishlist, name="remove_from_wishlist"),
    path("add/", views.add_product, name="add_product"),
    path("edit/<int:product_id>/", views.edit_product, name="edit_product"),
]
