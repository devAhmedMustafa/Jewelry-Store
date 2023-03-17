from django.db import models
from accounts.models import CustomUser as User
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Type(models.Model):

    name = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=120, null=True)
    price = models.FloatField(null=True)
    img = models.ImageField(upload_to='images/%y/%m/%d', null=True)
    description = models.CharField(max_length=4000, null=True)
    on_stock = models.BooleanField(default=True)
    left = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name

class Buying(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='requested')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    address = models.CharField(max_length=400)
    date = models.DateField(default=datetime.now, null=True)
    serial_key = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.product.name