from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle stripe web hooks
    """

    def __init__(self,request):
        self.request = request

    
    def handle_event(self, event):
        """
        Handle a generice/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook receiver: {event["type"]}',
            status=200
        )