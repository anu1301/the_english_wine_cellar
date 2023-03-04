from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_booking, name='view_booking'),
    path('book/<item_id>', views.book_now, name='book_now'),
]
