from django.urls import path
from . import views
from .views import view_wishlist

urlpatterns = [
    path('', views.view_profile, name='view_profile'),
    path('profile_wishlist/', view_wishlist, name='view_wishlist'),
    path('profile_settings/', views.profile_settings, name='profile_settings'),
    # path('alternative_profile_settings/', views.alternative_profile_settings, name='alternative_profile_settings'),
    path('orders_history/', views.orders_history, name='orders_history'),
    path('order_history/<order_id>', views.order_history, name='order_history'),
    path('delete_order/<str:order_id>', views.delete_order, name='delete_order'),
]