from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KT6XyKSWQ8RQNHSjSvlSnaTRk39FbxXfm8EXmey0pUz7zBVCiPfHRC5aE6daAZig3fG5g7QCzrPTX8hg9hiilwr00me3B8LaF',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)