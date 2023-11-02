from django.contrib import admin

from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    '''Customize the admin interface to display order line items'''
    model = OrderLineItem
    readonly_fields = ('line_item_total',)


class OrderAdmin(admin.ModelAdmin):
    '''Customize the admin interface to display order details'''

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_id', 'created', 'updated', 'delivery_cost',
                       'order_total', 'grand_total',)

    fields = ('order_id', 'first_name', 'last_name',
              'email_address', 'phone_number', 'street_address1',
              'street_address2', 'city', 'postal_code',
              'country', 'created', 'updated',
              'delivery_cost', 'order_total', 'grand_total',)

    list_display = (
        'order_id',
        'first_name',
        'last_name',
        'email_address',
        'phone_number',
        'street_address1',
        'street_address2',
        'city',
        'postal_code',
        'country',
        'order_total',
        'delivery_cost',
        'grand_total',
        'created',
        'updated',
        'paid',
    )

    ordering = ('-created',)


admin.site.register(Order, OrderAdmin)
