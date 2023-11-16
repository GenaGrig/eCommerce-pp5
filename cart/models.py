from django.db import models


class Cart(models.Model):
    '''A model to represent the shopping cart'''

    cart_id = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
