
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from decimal import Decimal

from django_countries.fields import CountryField

from products.models import Product
from wine_tasting.models import Experiences
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    original_booking = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """ Generates a random order number using UUID """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updates grand total each time a line item is added,
        takes into account delivery costs
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * \
                settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the order number
        if it hasn't been set already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

        def __str__(self):
            return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.CASCADE)
    experience = models.ForeignKey(Experiences, null=True, blank=True,
                                   on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False,)

    def get_price(self, *args, **kwargs):
        if self.product and self.experience:
            print("combo price")
            return self.product.price + self.experience.price
        elif self.product:
            print('product price')
            return self.product.price
        elif self.experience:
            print('exp price')
            return self.experience.price

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the lineitem total
        and updates the order total
        """

        self.price = self.get_price()
        self.lineitem_total = int(self.price) * self.quantity

        print("I'm saving")
        super().save(*args, **kwargs)

    def __str__(self):
        if self.product is None:
            return 'None'

        if self.experience is None:
            return 'None'

        return f'SKU {self.product.sku} on order {self.order.order_number}'
