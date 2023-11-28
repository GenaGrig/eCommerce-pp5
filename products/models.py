from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    ''' Model for product categories'''
    id = models.AutoField(primary_key=True)
    parent_category_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    category_name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

    def get_friendly_name(self):
        ''' Return friendly name if available '''
        return self.friendly_name


class Product(models.Model):
    ''' Model for products'''
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255, blank=True, null=True)
    product_color = models.CharField(max_length=255, blank=True, null=True)
    product_material = models.CharField(max_length=255, blank=True, null=True)
    product_brand = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_in_stock = models.IntegerField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    '''A user wishlist model for maintaining wishlist'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('products.Product', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def add_to_wishlist(self, product):
        ''' Add a product to the wishlist '''
        self.products.add(product)

    def remove_from_wishlist(self, product):
        ''' Remove a product from the wishlist '''
        self.products.remove(product)
        
    def __str__(self):
        return self.products.name
