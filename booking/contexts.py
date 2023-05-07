from decimal import Decimal
from datetime import datetime
from django.shortcuts import get_object_or_404

from wine_tasting.models import Experiences


def booking_contents(request):

    booking_items = []
    booking_total = 0
    experience_count = 0
    date = '22-April-2023'
    converted = datetime.strptime(date, '%d-%B-%Y')

    booking = request.session.get('booking', {})

    for item_id, item_data in booking.items():
        if isinstance(item_data, int):
            experience = get_object_or_404(Experiences, pk=item_id)
            booking_total += Decimal(item_data * experience.price)
            experience_count += item_data
            booking_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'experience': experience,
            })
        else:
            experience = get_object_or_404(Experiences, pk=item_id)
            for date, quantity in item_data['items_by_date'].items():
                booking_total += Decimal(quantity * experience.price)
                experience_count += quantity
                booking_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'experience': experience,
                    'date': date,
                })

    context = {
        'booking_items': booking_items,
        'booking_total': booking_total,
        'experience_count': experience_count,
    }

    return context
