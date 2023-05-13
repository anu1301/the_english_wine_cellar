from django.db import models
from django.db.models import Avg, Count
from django.contrib.auth.models import User
from products.models import Product


class ReviewRating(models.Model):
    """ Fields for adding product reviews """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
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
        return f'Review {self.subject} by {self.user}'

    def averageReview(request, product_id):
        reviews = ReviewRating.objects.filter(product=product_id, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(request, product_id):
        reviews = ReviewRating.objects.filter(product=product_id, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count
