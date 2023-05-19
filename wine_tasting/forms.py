from django import forms
from django.forms import ModelForm
from booking.models import Booking
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingDate(forms.ModelForm):
    """
    Enables users to make a booking.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['booking_date'].required = True

    class Meta:
        """
        Uses Booking Model to create the booking form
        """
        model = Booking
        fields = (
            'booking_date',
        )

        labels = {
            'booking_date': 'Select booking date',
        }

        widgets = {
              'booking_date': DateInput()
        }
