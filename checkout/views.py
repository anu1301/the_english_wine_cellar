from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your basket at the moment.')
        return redirect(reverse('products'))  # prevents manual access to URL by typing /checkout

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MH7bdCKM1yd4Jvji0TC2twQ68Vqv2RQlnqZZVb8GXRJvn70c7SrfL6zuCKCCHPtETVtaJkGmKVFuMzfnh99EJei00AoaCMM64',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
