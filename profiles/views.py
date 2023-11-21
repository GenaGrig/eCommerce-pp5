from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from products.models import Wishlist
from checkout.models import Order


def view_profile(request):
    '''Display the user's profile'''
    profile = get_object_or_404(UserProfile, user=request.user)
    user_profile = get_user_profile(request.user)
    
    form = UserProfileForm(instance=profile)
    orders = Order.objects.filter(user_profile=get_user_profile(request.user)).order_by('-created')[:3]

    template = 'profiles/profiles.html'
    context = {
        'form': form,
        'orders': orders,
        'user_profile': user_profile,
    }

    return render(request, template, context)


def view_alternative_profile(request):
    '''Display the user's alternative profile'''
    profile = get_object_or_404(UserProfile, user=request.user)
    user_profile = get_user_profile(request.user)
    
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profiles.html'
    context = {
        'form': form,
        'orders': orders,
        'user_profile': user_profile,
    }

    return render(request, template, context)


def get_user_profile(user):
    '''Get the user's profile'''
    try:
        return UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        return None


@login_required
def view_wishlist(request):
    '''View the user's wishlist'''
    wishlist = get_object_or_404(Wishlist, user=request.user)

    template = 'profiles/wishlist_profile.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


def profile_settings(request):
    '''Display the user's profile settings'''
    profile_settings = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile_settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    
    form = UserProfileForm(instance=profile_settings)

    template = 'profiles/profile_settings.html'
    context = {
        'form': form,
        'on_profile_settings_page': True,
    }

    return render(request, template, context)


# def alternative_profile_settings(request):
#     '''Display the user's alternative profile settings'''
#     alternative_profile_settings = get_object_or_404(UserProfile, user=request.user)
    
#     if request.method == 'POST':
#         form = AlternativeUserProfileForm(request.POST, instance=alternative_profile_settings)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Alternative profile settings updated successfully')
    
#     form = AlternativeUserProfileForm(instance=alternative_profile_settings)

#     template = 'profiles/profile_settings.html'
#     context = {
#         'form': form,
#         'on_profile_settings_page': True,
#     }

#     return render(request, template, context)


def orders_history(request):
    '''Display the user's order history'''
    profile = get_object_or_404(UserProfile, user=request.user)
    user_profile = get_user_profile(request.user)
    
    form = UserProfileForm(instance=profile)
    orders = Order.objects.filter(user_profile=get_user_profile(request.user)).order_by('-created')
    
    template = 'profiles/orders_history.html'
    context = {
        'form': form,
        'orders': orders,
        'user_profile': user_profile,
    }

    return render(request, template, context)


def order_history(request, order_id):
    '''Display the user's order history'''
    order = Order.objects.filter(user_profile=request.user.user_profile).order_by('-created')[:3]

    messages.info(request, (
        f'This is a past confirmation for order number {order_id}. '
        'A confirmation email was sent on the order date.'
    ))
    
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)