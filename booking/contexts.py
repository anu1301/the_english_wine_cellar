

def booking_contents(request):

    booking_items = []
    total = 0
    experience_count = 0

    context = {
        'booking_items': booking_items,
        'total': total,
        'experience_count': experience_count,
    }

    return context
