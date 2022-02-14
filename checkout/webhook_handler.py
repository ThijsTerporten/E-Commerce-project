from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle stripe web hooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generice/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payement_intent_succeeded(self, event):
        """
        Handle payment intent succeseeded webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payement_intent_payment_failed(self, event):
        """
        Handle payment intent failed webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
