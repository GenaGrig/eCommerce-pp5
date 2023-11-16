import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.utils import timezone

from django_countries.fields import CountryField
from products.models import Product


class Order(models.Model):
    '''Create an order model to store order details'''
    order_id = models.CharField(max_length=50, null=False, editable=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.EmailField(max_length=250, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False, default='')
    building_number1 = models.CharField(max_length=80, null=False, blank=False, default='')
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    building_number2 = models.CharField(max_length=80, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=50, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    coupon = models.ForeignKey('GiftCoupon', null=True, blank=True, on_delete=models.SET_NULL)

    def _generate_order_id(self):
        '''Generate a random, unique order id using UUID'''
        return uuid.uuid4().hex.upper()

    def update_total(self):
        '''Update grand total each time a line item is added, accounting
        for delivery costs'''
        line_item_totals = self.line_items.values_list('line_item_total', flat=True)
        print(f"Line item totals: {line_item_totals}")  # Add this line for debugging
        
        self.order_total = self.line_items.aggregate(Sum('line_item_total'))['line_item_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total + settings.STANDARD_DELIVERY_COST
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        
        # Check if a coupon is applied before subtracting its value
        if self.coupon:
            print(f"Order total before discount: {self.order_total}")  # Add this line for debugging
            print(f"Coupon value: {self.coupon.coupon_value}")  # Add this line for debugging
            self.grand_total -= self.coupon.coupon_value
        self.save()

    def save(self, *args, **kwargs):
        '''Override the original save method to set the order id if it
        hasn't been set already'''
        
        if not self.order_id:
            self.order_id = self._generate_order_id()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'


class OrderLineItem(models.Model):
    '''Create an order line item model to store order line item details'''
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='line_items')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        '''Override the original save method to set the line item total and
        update the order total'''
        self.line_item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_id}'


class GiftCoupon(models.Model):
    '''Create a gift coupon model to store gift coupon details'''
    coupon_id = models.CharField(max_length=50, null=False, editable=False)
    coupon_code = models.CharField(max_length=50, null=False, blank=False)
    coupon_value = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    coupon_expiry = models.DateField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    description = models.CharField(max_length=250, null=False, blank=False)

    def _generate_coupon_id(self):
        '''Generate a random, unique coupon id using UUID'''
        return uuid.uuid4().hex.upper()
    
    def is_valid(self):
        '''Check if the coupon is valid'''
        return self.active and self.coupon_expiry >= timezone.now().date()

    def save(self, *args, **kwargs):
        '''Override the original save method to set the coupon id if it
        hasn't been set already'''
        
        if not self.coupon_id:
            self.coupon_id = self._generate_coupon_id()
        super().save(*args, **kwargs)
        
        if self.coupon_expiry < timezone.now().date():
            raise ValueError('Coupon has expired')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Coupon {self.coupon_id}'
