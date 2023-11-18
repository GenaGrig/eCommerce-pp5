from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from products.models import Wishlist


def view_profile(request):
    '''Display the user's profile'''
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profiles.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def view_wishlist(request):
    '''View the user's wishlist'''
    wishlist = get_object_or_404(Wishlist, user=request.user)

    template = 'profiles/wishlist_profile.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)
