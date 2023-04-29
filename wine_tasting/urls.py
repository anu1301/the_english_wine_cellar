from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_experiences, name='experiences'),
    path('<experience_id>/', views.experience_detail, name='experience_detail'),
]
