from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter_sub, name='newsletter'),
]