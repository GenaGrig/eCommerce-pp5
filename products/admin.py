from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Category, Subscriber, Review


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
    
    
class SubscriberAdmin(admin.ModelAdmin):
    ''' Admin view for subscribers'''
    list_display = (
        'email',
        'date_added',
    )
    search_fields = ('email',)

    ordering = ('email',)
    
    
class ReviewAdmin(admin.ModelAdmin):
    ''' Admin view for reviews'''
    list_display = (
        'product',
        'user',
        'rating',
        'date_added',
    )

    ordering = ('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Review, ReviewAdmin)
