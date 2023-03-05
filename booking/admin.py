from django.contrib import admin
from .models import Booking, BookingItem


class BookingItemAdminInline(admin.TabularInline):
    model = BookingItem
    readonly_fields = ('bookingitem_total',)


class BookingAdmin(admin.ModelAdmin):
    inlines = (BookingItemAdminInline,)

    readonly_fields = ('booking_total', 'booking_ref', 'stripe_pid',)

    list_display = (
        'booking_ref',
        'full_name',
        'booking_date',
        'booking_total',
        'status',
    )

    ordering = ('booking_date',)


admin.site.register(Booking, BookingAdmin)
