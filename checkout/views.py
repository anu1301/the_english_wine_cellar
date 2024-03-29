from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from wine_tasting.models import Experiences
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.contexts import bag_contents
from booking.contexts import booking_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):

    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'booking': json.dumps(request.session.get('booking', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        booking = request.session.get('booking', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.original_booking = json.dumps(booking)
            order.save()

            if len(bag.items()):
                print("items are in the bag session context")

            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for quantity in item_data['quantity'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our \
                            database."
                        "Please contact us for further assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            order = order_form.save(commit=False)
            if len(booking.items()):
                print("items are in the booking session context")
                print('booking', booking.items)

            for item_id, date_number_people in booking.items():
                print('item_id', item_id)
                print('date_number_people', date_number_people)

                try:
                    experience = Experiences.objects.get(pk=item_id)
                    if isinstance(date_number_people, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            experience=experience,
                            quantity=quantity,
                        )
                        order_line_item.save()
                    else:
                        for date_val in date_number_people["items_by_date"]:
                            num_people = date_number_people["items_by_date"][date_val]
                            print('num_people', num_people)
                            order_line_item = OrderLineItem(
                                order=order,
                                experience=experience,
                                quantity=num_people,
                            )
                            order_line_item.save()
                except Experiences.DoesNotExist:
                    messages.error(request, (
                        "One of the experiences in your booking wasn't found \
                            in our database."
                        "Please contact us for further assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_booking'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]
            ))

        else:
            messages.error(request, 'There was an error with your form. \
                Please check your information again.')

    # For any other request that is not a post
    else:
        booking = request.session.get('booking', {})
        bag = request.session.get('bag', {})
        if not bag and not booking:
            messages.error(
                request, 'There is nothing in your basket at the moment.')
            # prevents manual access to URL by typing /checkout
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        current_experiences = booking_contents(request)
        total = current_bag['grand_total'] + \
            current_experiences['booking_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
             Have you forgotten to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handles successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order succesfully placed! \
        Your order number is: {order_number}. \
            Your order will be confirmed shortly.')

    if 'bag' in request.session:
        del request.session['bag']

    if 'booking' in request.session:
        del request.session['booking']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
