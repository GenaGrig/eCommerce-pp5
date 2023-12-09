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
    path("delete/<int:product_id>/", views.delete_product, name="delete_product"),
    path('subscribe/', views.subscribe_to_newsletter, name='subscribe_to_newsletter'),
    path('unsubscribe/', views.unsubscribe_from_newsletter, name='unsubscribe_from_newsletter'),
    path('404', views.page_not_found, name='404'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
]
