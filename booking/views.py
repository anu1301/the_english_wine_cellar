from django.shortcuts import render, redirect, reverse
# get_object_or_404
from django.contrib import messages
from datetime import datetime

# from .forms import BookingForm, BookingItemForm
from .models import BookingItem, Booking
# from wine_tasting.models import Experiences


def view_booking(request):
    """ A view that renders the booking page """

    return render(request, 'booking/booking.html')


def book_now(request, item_id):
    """ Add a number of people and date of the experience to booking """

    quantity = int(request.POST.get('quantity'))
    # date = datetime(request.POST.get('date'))
    redirect_url = request.POST.get('redirect_url')
    booking = request.session.get('booking', {})

    if item_id in list(booking.keys()):
        booking[item_id] += quantity
        # messages.success(
            # request, f'Updated {experiences.name} quantity to {booking[item_id]}')
    else:
        booking[item_id] = quantity
        # messages.success(request, f'Added {experiences.name} to your booking')

    # if item_id in list(booking.keys()):
    #     booking[item_id] += date
    #     messages.success(
    #         request, f'Updated {experience.name} date to {booking[item_id]}')
    # else:
    #     booking[item_id] = date
    #     messages.success(request, f'Added {experience.name} to your booking')
   
    request.session['booking'] = booking
    print(request.session['booking'])
    return redirect(redirect_url)



# def bookingitem(request):
#     """ A view that shows the booking page """

#     number_of_people = BookingItem.objects.get(number_of_people)

#     template = 'booking/booking.html'
#     context = {
#         'number_of_people': number_of_people,
#     }

#     return render(request, template, context)


# def add_to_form(request, exp_id):
#     """ Add specified product to the booking form """

#     form_items = []

#     experience = get_object_or_404(Experiences, pk=exp_id)

#     booking_form = BookingForm()
#     bookingitem_form = BookingItemForm()
#     template = 'booking/booking.html'
#     context = {
#         'booking_form': booking_form,
#         'bookingitem_form': bookingitem_form,
#         'experience': experience,
#         'form_items': form_items,
#     }
#     return render(request, template, context)
