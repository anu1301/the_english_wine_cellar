from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import BookingItem


@receiver(post_save, sender=BookingItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update booking total on bookingitem update/create
    """

    instance.booking.update_total()


@receiver(post_delete, sender=BookingItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update booking total on bookingitem delete
    """
    instance.booking.update_total()
