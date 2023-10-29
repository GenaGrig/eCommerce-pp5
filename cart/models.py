from django.db import models


class Coupon(models.Model):
    '''A model to represent discount coupons'''

    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField()

    def __str__(self):
        return self.code
