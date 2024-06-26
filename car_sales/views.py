from django.shortcuts import render,get_object_or_404
from cars.models import Car
from brand.models import  Brand






def home(request, brand_slug=None):
    cars = Car.objects.all()  
    brands = Brand.objects.all()  
    if brand_slug:
        brand = Brand.objects.get(slug=brand_slug)
        cars = cars.filter(brand=brand)  
    return render(request, 'home.html', {'data': cars, 'brands': brands})







