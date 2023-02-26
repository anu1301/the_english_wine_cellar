from django.db import models
from django.contrib.auth.models import User
from wine_tasting.models import Experiences

import uuid

STATUS = ((1, 'Confirmed'), (0, 'Not Confirmed'))
EXPERIENCELIST = {}


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')
    booking_ref = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    experience_choice = models.ForeignKey(Experiences, on_delete=models.CASCADE, max_length=150, related_name='experience_list')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    number_of_people = models.IntegerField(default=1, null=False, blank=False)
    booking_date = models.DateField(auto_now=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-booking_date']

    # def booking_total(self, *args, **kwargs):
    #     """
    #    Sets booking total
    #     """
    #     self.booking_total = self.experiences.price * self.number_of_people
    #     super().save(*args, **kwargs)
