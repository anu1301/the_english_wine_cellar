from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from datetime import datetime

from .models import BookingItem, Booking
from wine_tasting.models import Experiences


def view_booking(request):
    """ A view that renders the booking page """

    return render(request, 'booking/booking.html')


def add_to_booking(request, item_id):
    """ Add a number of people and date of the experience to booking """

    experience = get_object_or_404(Experiences, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    booking = request.session.get('booking', {})

    if item_id in list(booking.keys()):
        booking[item_id] += quantity
    else:
        booking[item_id] = quantity
        messages.success(request, f'Added {experience.name} to your booking')

    request.session['booking'] = booking
    return redirect(redirect_url)


def adjust_booking(request, item_id):
    """
    Adjust the quantity of the specified experience to the specified amount
    """

    experience = get_object_or_404(Experiences, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    booking = request.session.get('booking', {})

    if quantity > 0:
        booking[item_id] = quantity
    else:
        booking.pop(item_id)
        messages.success(
            request, f'Removed {experience.name} from your booking')

    request.session['booking'] = booking
    return redirect(reverse('view_booking'))


def remove_from_booking(request, item_id):
    """ Removes specified experience from the booking """

    try:
        experience = get_object_or_404(Experiences, pk=item_id)
        item = None
        if 'item_id' in request.POST:
            item = request.POST['item_id']
        booking = request.session.get('booking', {})

        if item:
            del booking[item_id]["item_id"]
            messages.success(
                request, f'Removed {experience.name} from your booking')
        else:
            booking.pop(item_id)
            messages.success(
                request, f'Removed {experience.name} from your booking')

        request.session['booking'] = booking
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
