from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from datetime import datetime, date

from .models import BookingItem, Booking
from wine_tasting.models import Experiences
from .forms import BookingForm


def view_booking(request):
    """ A view that renders the booking page """

    return render(request, 'booking/booking.html')


def add_to_booking(request, item_id):
    """ Add a number of people and date of the experience to booking """

    experience = get_object_or_404(Experiences, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    date = str(request.POST.get('date'))
    booking = request.session.get('booking', {})

    if item_id in list(booking.keys()):
        if item_id and date in booking[item_id]['items_by_date'].keys():
            booking[item_id]['items_by_date'][date] += quantity
            messages.success(
                request, f'Updated {experience.name} \
                    quantity to {booking[item_id]}')
        else:
            booking[item_id]['items_by_date'][date] = quantity
            messages.success(
                request, f'Added {experience.name} to your booking')
    else:
        booking[item_id] = {'items_by_date': {date: quantity}}
        messages.success(request, f'Added {experience.name} to your booking')

    request.session['booking'] = booking
    return redirect(redirect_url)


def adjust_booking(request, item_id):
    """
    Adjust the quantity of the specified experience to the specified amount
    """
    experience = get_object_or_404(Experiences, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    date = str(request.POST.get('date'))
    booking = request.session.get('booking', {})

    if quantity > 0:
        booking[item_id] = {'items_by_date': {date: quantity}}
        messages.success(request, f'Updated {experience.name} in your booking')
    else:
        del booking[item_id]['items_by_date'][date]
        if not booking[item_id]['items_by_date'][date]:
            booking.pop(booking[item_id]['items_by_date'].keys())
            messages.success(
                request, f'Removed {experience.name} from your booking')

    request.session['booking'] = booking
    return redirect(reverse('view_booking'))


def remove_from_booking(request, item_id):
    """ Removes specified experience from the booking """
    try:
        experience = get_object_or_404(Experiences, pk=item_id)
        date = str(request.POST.get('date'))
        booking = request.session.get('booking', {})

        if booking[item_id]['items_by_date']:
            booking.pop(item_id)

        request.session['booking'] = booking
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
