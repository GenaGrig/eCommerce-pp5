from django import template
from django.urls import reverse


register = template.Library()


@register.simple_tag
def breadcrumb(category):
    ''' Return the breadcrumb for the given category'''
    breadcrumbs = []
    while category:
        breadcrumbs.insert(0, {'name': category.friendly_name, 
                               'url': reverse('products_in_category',
                                              args=[category.id])})
        category = category.parent_category_id

    return breadcrumbs
