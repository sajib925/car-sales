from django.contrib import admin
from django.urls import path
from .views import AddBrandView 

urlpatterns = [
    path('add_brand/', AddBrandView.as_view(), name='add_brand'),
]
