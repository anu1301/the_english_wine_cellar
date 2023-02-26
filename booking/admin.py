from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    # readonly_fields = ('booking_total',)

    list_display = (
        'booking_ref',
        'experience_choice',
        'number_of_people',
        'booking_date',
        'status',
    )

    ordering = ('booking_date',)


admin.site.register(Booking, BookingAdmin)
