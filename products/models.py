from django.db import models


class Category(models.Model):
    ''' Model for product categories'''
    id = models.AutoField(primary_key=True)
    parent_category_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    category_name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    ''' Model for products'''
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_in_stock = models.IntegerField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def __str__(self):
        return self.name