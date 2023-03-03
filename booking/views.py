from django.shortcuts import render
# , redirect, reverse, get_object_or_404
# from django.contrib import messages

# from .forms import BookingForm, BookingItemForm
# from .models import BookingItem
# from wine_tasting.models import Experiences


def view_booking(request):
    """ A view that renders the booking page """

    return render(request, 'booking/booking.html')


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
#     print(form_items)
#     return render(request, template, context)
