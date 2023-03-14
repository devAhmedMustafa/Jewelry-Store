from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User
from .forms import NewUserForm
from accounts.models import CustomUser
from .models import ShippingData
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import json
# Create your views here.

def login(request):

    error = ''

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        existCheck = CustomUser.objects.filter(email__iexact = email).exists()

        if existCheck:

            user = authenticate(email=email, password=password)

            if user is not None:

                print(password)

                userData = CustomUser.objects.get(email=email)
                
                auth_login(request, user)

                return redirect('home')
            
        else:
            error = 'Invalid Login'

    return render(request, 'login.html', {'error':error})

def signup(request):

    if request.method == 'POST':
        form = NewUserForm(request.POST) 
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    
    form = NewUserForm()

    return render(request, 'signup.html', {'form':form})

def user_validation(request):

    email = request.GET.get('email')
    is_taken = CustomUser.objects.filter(email__iexact=email).exists()

    data = {'is_taken': is_taken}

    return JsonResponse(data)


@login_required
def profile(request):

    user = request.user

    if ShippingData.objects.filter(user=user).exists():

        shippingData = ShippingData.objects.get(user=user)
        
        return render(request, 'profile.html',{'user':user, 'shipData': shippingData})
    
    else:
        return redirect('complete_data')

@login_required
def logout(request):

    auth_logout(request)

    return redirect('home')


@login_required
def complete_data(request):

    user = request.user
    
    with open('JSONs/cities.json', encoding='utf-8') as f:
        cities = json.load(f)

    if request.method == 'POST':

        phone_number = request.POST['phone_number']
        address = request.POST['address']
        city = request.POST['city']

        data = ShippingData(user=user, phone_number=phone_number, address= address, city=city)
        data.save()

        return redirect('home')

    return render(request, 'complete_data.html', {'data':cities["city"], 'message':'Done'})