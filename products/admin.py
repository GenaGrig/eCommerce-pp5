from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
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
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'category_name',
    )
    
    ordering = ('category_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
