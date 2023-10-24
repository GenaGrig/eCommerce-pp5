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
    

class ProductInline(admin.TabularInline):
    ''' Admin view for products in categories'''
    model = Product
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    ''' Admin view for categories'''
    inlines = [ProductInline]
    list_display = (
        'friendly_name',
        'category_name',
        'id',
    )

    ordering = ('category_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
