from django.shortcuts import render, redirect
from .models import Type, Product, Cart, Buying
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from . import functions
import json
from django.contrib.auth.decorators import login_required
from accounts.models import ShippingData
from django.db.models import F, Q

# Create your views here.

def home(reqeust):

    functions.check_left()
    
    types = Type.objects.all()
    products = Product.objects.all()

    user = reqeust.user

    return render(reqeust, 'home.html',{'types':types, 'products':products, 'user':user})

def product(request, productId):

    types = Type.objects.all()

    product = Product.objects.get(pk = productId)

    user = request.user

    return render(request, 'product.html', {'product': product, 'user':user, 'types':types})

def jewelry(request, typeId):

    types = Type.objects.all()

    jewelry = Type.objects.get(pk = typeId)

    products = Product.objects.filter(type=jewelry)

    return render(request,'jewelry.html', {'products': products, 'types':types, 'jewelry':jewelry})

def search(request):

    search_input = request.GET.get('searchInput')

    data = {
        'products': json.dumps(list(Product.objects.filter(name__icontains = search_input).values())),
        'does_exist': Product.objects.filter(name__icontains = search_input).exists(),
    }
    
    return JsonResponse(data)

@login_required
def cart(request):

    types = Type.objects.all()

    user = request.user

    cartProducts = Cart.objects.filter(user=user)

    return render(request, 'cart.html', {'products':cartProducts, 'types':types})

@login_required
def add_to_cart(request, productId):

    product = Product.objects.get(pk=productId)
    user = request.user

    if request.method == 'POST':

        quantity = request.POST['quantity']

        if Cart.objects.filter(user = user, product= product).exists():
            return render(request, 'product.html', {'product': product, 'user':user})

        else:
            
            cart = Cart(product=product, user = user, quantity= quantity)
            cart.save()

    return redirect('cart')

@login_required
def buy_now(request, productId):

    user = request.user

    if ShippingData.objects.filter(user=user).exists():

        product = Product.objects.get(pk=productId)
        
        ship_data = ShippingData.objects.get(user=user)

        return render(request, 'buy_now.html', {'product':product, 'user':user,'ship_data':ship_data})
    
    else:
        return redirect('complete_data')

@login_required
def delete_from_cart(request, productId):

    user = request.user

    if request.method == 'POST':

        product = Product.objects.get(pk=productId) # product to be deleted
        Cart.objects.get(product=product, user=user).delete()

    return redirect('cart')

@login_required
def complete_buying(request, productId):

    
    user = request.user
    ship_data = ShippingData.objects.get(user=user)

    if request.method == 'POST':

        product = Product.objects.get(pk=productId)
        quantity = Cart.objects.get(product=product, user=user).quantity

        if Product.objects.get(pk=productId).left != 0:

            address = request.POST['address']
            
            Product.objects.filter(pk=productId).update(left=F('left') - int(quantity))

            data = Buying(user=user, product=product, quantity=quantity, address=address, serial_key=functions.add_serial_key())
            data.save()
            
            Cart.objects.get(product=product, user=user).delete()
            return render(request, 'done_process.html', {'message':'Your Payment process is done'})
    
    return HttpResponse('Done')

@login_required
def buyings(request):

    types = Type.objects.all()

    user = request.user

    boughtProducts = Buying.objects.filter(user=user)

    return render(request, 'buyings.html', {'products':boughtProducts, 'types':types})

def quantity_validate(request):

    quant_request = int(request.GET.get('quantity'))
    quantity_in_stock = int(request.GET.get('quantity_in_stock'))
    validation = False

    if quant_request > quantity_in_stock or quant_request == 0:
        validation = True

    print(quantity_in_stock)

    data = {
        'validation': validation
    }

    return JsonResponse(data)

@login_required
def order_requests(request):

    user = request.user

    if user.is_superuser == True and user.is_staff == True:
        
        ship_data = ShippingData.objects.get(user=user)
        orders = Buying.objects.filter(Q(status__iexact = 'requested'))

        return render(request, 'orders.html', {'orders':orders, 'title': 'Orders', 'ship_data':ship_data, 'user':user})

    else:
        return redirect('buyings')
    
@login_required
def being_delivered(request):

    user = request.user

    if user.is_superuser == True and user.is_staff == True:
        
        ship_data = ShippingData.objects.get(user=user)
        orders = Buying.objects.filter(Q(status__iexact = 'on_your_way'))

        return render(request, 'orders.html', {'orders':orders, 'title': 'Being Delivered', 'ship_data':ship_data, 'user':user})

    else:
        return redirect('buyings')
    
@login_required
def delivered(request):

    user = request.user

    if user.is_superuser == True and user.is_staff == True:
        
        ship_data = ShippingData.objects.get(user=user)
        orders = Buying.objects.filter(Q(status__iexact = 'delivered'))

        return render(request, 'orders.html', {'orders':orders, 'title': 'Delivered', 'ship_data':ship_data, 'user':user})

    else:
        return redirect('buyings')

def orders_status(request):
    
    status = request.GET.get('status')
    order_id = request.GET.get('order_id')

    order = Buying.objects.get(pk=order_id)

    data = {

    }

    if status == 'requested':

        data['status'] = 'on_your_way'
        
        order.status = 'on_your_way'
        order.save()

    elif status == 'on_your_way':

        data['status'] = 'delivered'

        order.status = 'delivered'
        order.save()
    
    return JsonResponse(data)