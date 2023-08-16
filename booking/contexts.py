from decimal import Decimal
from datetime import datetime
from django.conf import settings
from django.shortcuts import get_object_or_404
from wine_tasting.models import Experiences


def booking_contents(request):

    booking_items = []
    booking_total = 0
    experience_count = 0

    booking = request.session.get('booking', {})

    # print('booking items: ', booking.items())
    for item_id, date_number_people in booking.items():
        # print('item_id: ', item_id)
        # print('date_num_people: ', date_number_people)
        experience = get_object_or_404(Experiences, pk=item_id)
        # print("experience", experience)

        for date_val in date_number_people["items_by_date"]:
            print('date_val: ', date_val)
            num_people = date_number_people["items_by_date"][date_val]
            print('num_people: ', num_people)
            booking_total += num_people * experience.price
            experience_count += num_people

            booking_items.append({
                'item_id': item_id,
                'quantity': num_people,
                'experience': experience,
                'date': date_val,
            })
            print('booking', booking_items)

    context = {
        'booking_items': booking_items,
        'booking_total': booking_total,
        'experience_count': experience_count,
    }

    return context
