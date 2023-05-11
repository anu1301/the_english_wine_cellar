from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from wine_tasting.models import Experiences


class ReviewRating(models.Model):
    """ Fields for adding product reviews """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experiences, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, help_text='Add your review title here')
    review = models.TextField(max_length=500, help_text='Add your review here')
    rating = models.FloatField()
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Review {self.subject} by {self.User}'
