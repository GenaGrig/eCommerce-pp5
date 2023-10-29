from django.db import models


class Coupon(models.Model):
    '''A model to represent discount coupons'''

    coupon_code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount_price = models.IntegerField(default=100)
    isExpired = models.BooleanField(default=False)
    minimum_price = models.IntegerField(default=0)

    def __str__(self):
        return self.code


class Cart(models.Model):
    '''A model to represent the shopping cart'''

    cart_id = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.cart_id
