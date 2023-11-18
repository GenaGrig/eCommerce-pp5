from django.shortcuts import render


def view_profile(request):
    '''Display the user's profile'''
    template = 'profiles/profiles.html'
    context = {
        'on_profile_page': True
    }
    return render(request, template, context)
