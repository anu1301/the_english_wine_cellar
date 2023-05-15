from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter_sub, name='newsletter'),
    path(
        'newsletter/unsubscribe',
        views.newsletter_unsubscribe,
        name='newsletter_unsubscribe'),
]