from django.db import models
from django.contrib.auth import get_user_model
from brand.models import Brand



class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.title

class Comment(models.Model):
    car = models.ForeignKey(Car, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} on {self.car.title}'

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)