from django.urls import path
from . import views
from .webhooks import webhook
from .views import apply_gift_coupon

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_id>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('apply_gift_coupon/', apply_gift_coupon, name='apply_gift_coupon'),
]
