from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jewelry/<int:typeId>/', views.jewelry, name='jewelry'),
    path('product/<int:productId>/', views.product, name='product'),
    path('addToCart/<int:productId>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name = 'cart'),
    path('buynow/<int:productId>/', views.buy_now, name='buy_now'),
    path('DeleteFromCart/<int:productId>/', views.delete_from_cart, name='delete_from_cart'),
    path('ajax/search/', views.search, name='search'),
    path('complete_buying/<int:productId>', views.complete_buying, name='complete_buying'),
    path('buyings/', views.buyings, name='buyings'),
    path('ajax/quantity_validate/', views.quantity_validate, name='quantity_validate'),
    path('orders/', views.order_requests, name='orders'),
    path('delivered', views.delivered, name='delivered'),
    path('being_delivered', views.being_delivered , name='being_delivered'),
    path('ajax/order_status/', views.orders_status, name='order_status'),
]
