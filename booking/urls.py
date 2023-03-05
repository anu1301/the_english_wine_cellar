from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_booking, name='view_booking'),
    path('book/<item_id>', views.add_to_booking, name='add_to_booking'),
    path('adjust/<item_id>', views.adjust_booking, name='adjust_booking'),
    path('remove/<item_id>/', views.remove_from_booking, name='remove_from_booking'),
]
