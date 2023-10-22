from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Category


class ProductAdmin(SummernoteModelAdmin):
    ''' Admin view for products'''
    list_display = (
        'sku',
        'name',
        'category_id',
        'price',
        'quantity_in_stock',
        'rating',
        'image',
    )

    ordering = ('sku',)
    summernote_fields = ('short_description', 'description',)


class CategoryAdmin(admin.ModelAdmin):
    ''' Admin view for categories'''
    list_display = (
        'friendly_name',
        'category_name',
    )

    ordering = ('category_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
