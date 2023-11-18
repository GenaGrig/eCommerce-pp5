from django.urls import path
from . import views
from .views import view_wishlist

urlpatterns = [
    path('', views.view_profile, name='view_profile'),
    path('profiles/', view_wishlist, name='view_wishlist'),
]