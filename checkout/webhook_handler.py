from django.http import HttpResponse
import stripe
from .models import Order


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        
        try:
            # Check if 'cart' is present in metadata
            cart = intent.metadata.get('cart', {})
            save_info = intent.metadata.get('save_info')
        
            # Get the Charge object
            stripe_charge = stripe.Charge.retrieve(
                intent.latest_charge
            )

            billing_details = stripe_charge.billing_details
            shipping_details = intent.shipping
            grand_total = round(stripe_charge.amount / 100, 2)
            
            order_id = self.request.POST.get('order_id')

            if order_id:
                try:
                    order = Order.objects.get(pk=order_id)
                    print("Order Details:")
                    print("Order ID:", order.id)
                    print("Grand Total:", grand_total)

                except Order.DoesNotExist:
                    print("Order not found for ID:", order_id)
            else:
                print("Order ID not found in metadata.")
                
        except KeyError as e:
            print("KeyError:", e)
            print('Cart data not found in metadata.')
        
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
        
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
