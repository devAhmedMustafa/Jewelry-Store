from django.contrib import admin
from .models import Product, Type, Cart, Buying
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Type)
admin.site.register(Buying)