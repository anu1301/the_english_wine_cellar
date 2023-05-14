from django.db import models


class Experiences(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='')
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
