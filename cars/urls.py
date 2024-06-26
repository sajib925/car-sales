from django.urls import path
from . import views

urlpatterns = [
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('buy/<int:pk>/', views.buy_car, name='buy_car'),
]
