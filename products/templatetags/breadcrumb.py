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


@register.simple_tag
def product_breadcrumb(product):
    ''' Return the breadcrumb for the given product'''
    category = product.category
    breadcrumbs = breadcrumb(category)

    # Add the product to the breadcrumb
    breadcrumbs.append({'name': product.name, 'url': ''})

    return breadcrumbs
