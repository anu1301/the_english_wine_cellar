from decimal import Decimal
from datetime import datetime
from django.shortcuts import get_object_or_404

from wine_tasting.models import Experiences


def booking_contents(request):

    booking_items = []
    booking_total = 0
    experience_count = 0
    booking = request.session.get('booking', {})

    for item_id, quantity in booking.items():
        experience = get_object_or_404(Experiences, pk=item_id)
        booking_total += Decimal(quantity * experience.price)
        experience_count += quantity
        booking_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'experience': experience,
        })

    context = {
        'booking_items': booking_items,
        'booking_total': booking_total,
        'experience_count': experience_count,
    }

    return context
