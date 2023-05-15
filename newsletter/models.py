from django.db import models


class NewsLetterSub(models.Model):
    """ User newsletter subscription """

    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
