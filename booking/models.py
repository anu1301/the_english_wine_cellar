from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from decimal import Decimal
from django.core.exceptions import ValidationError

from wine_tasting.models import Experiences
from profiles.models import UserProfile

import uuid
import datetime


STATUS = ((1, 'Confirmed'), (0, 'Not Confirmed'))
EXPERIENCELIST = {}


def validate_date(value):
    today = datetime.date.today()
    if value <= today:
        raise ValidationError("Date cannot be today or in the past!")


class Booking(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='booking')
    booking_ref = models.CharField(
        primary_key=True, max_length=32,
        null=False, editable=False, default='')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    booking_date = models.DateField(
        validators=[validate_date], blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    booking_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_booking = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    class Meta:
        ordering = ['-booking_date']

    def _generate_booking_ref(self):
        """
        Generate a random unique booking ref using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Overides the original save method to set the booking ref 
        if it hasn't been set already
        """

        if not self.booking_ref:
            self.booking_ref = self._generate_booking_ref()
        super().save(*args, **kwargs)

        def __str__(self):
            return self.booking_ref


class BookingItem(models.Model):
    bookings = models.ForeignKey(
        Booking, null=False, blank=False, on_delete=models.CASCADE,
        related_name='bookingitem')
    experience = models.ForeignKey(
        Experiences, null=False, blank=False, on_delete=models.CASCADE)
    number_of_people = models.IntegerField(
        default=1, null=False, blank=False)
    bookingitem_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False,
        blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the bookingitem total 
        and updates the booking total
        """
        self.bookingitem_total = Decimal(
            self.experience.price * self.number_of_people)
        super().save(*args, **kwargs)

        def __str__(self):
            return f'Experience {self.experience.name} on booking {self.bookings.booking_ref}'
