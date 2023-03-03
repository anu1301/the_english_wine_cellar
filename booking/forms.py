from django import forms
from .models import Booking, BookingItem


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('full_name', 'email', 'phone_number', 'experience_choice', 'booking_date',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and sets autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'experience_choice': 'Experience Choice',
            'booking_date': 'Booking Date',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class BookingItemForm(forms.ModelForm):
    class Meta:
        model = BookingItem
        fields = ('number_of_people',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholder
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'number_of_people': 'Number of People'
        }
