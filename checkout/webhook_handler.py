import logging

from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

import stripe

from .models import Order

logger = logging.getLogger(__name__)


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request
        
    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email_address
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

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
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        try:
            # Get the Charge object
            stripe_charge = stripe.Charge.retrieve(
                intent.latest_charge
            )

            billing_details = stripe_charge.billing_details
            shipping_details = intent.shipping
            grand_total = round(stripe_charge.amount / 100, 2)
            
            order = self.request.POST.get('order.id')

            if order:
                try:
                    order = Order.objects.get(pk=order.id)

                except Order.DoesNotExist:
                    print("Order not found for ID:", order.id)
            else:
                print("Order ID not found in metadata.")
                
        except KeyError as e:
            print("KeyError:", e)
            print('Cart data not found in metadata.')
        self._send_confirmation_email(order)
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
