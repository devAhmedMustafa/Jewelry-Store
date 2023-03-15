from django.contrib import admin
from .models import Product, Type, Cart, Buying
# Register your models here.

admin.site.site_header = "Fefel Jewels"

class InlineProduct(admin.StackedInline):
    model = Product
    extra = 1

class TypeAdmin(admin.ModelAdmin):
    inlines = [InlineProduct]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('type', 'price', 'left')
    list_editable = ('price',)
    list_filter = ('type', 'on_stock')
    search_fields = ('name', 'type')

admin.site.register(Product , ProductAdmin)
admin.site.register(Cart)
admin.site.register(Type, TypeAdmin)
admin.site.register(Buying)