from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('ajax/user_validate/', views.user_validation, name='user_validate'),
    path('complete_data/', views.complete_data, name='complete_data')
]
