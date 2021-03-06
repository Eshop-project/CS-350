from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as Accounts

from django.views.generic import DetailView

#Create views here
from .models import *
from .forms import OrderForm, CreateUserForm
from .utils import cookieCart, cartData, guestOrder

class productview(DetailView):
    model = Product
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        context = super(productview, self).get_context_data(**kwargs)
        data = cartData(self.request)
        cartItems = data['cartItems']  
        context['cartItems'] = cartItems
        return context
        

def registerPage(request):
    data = cartData(request)
    cartItems = data['cartItems']
    if request.user.is_authenticated:
        return redirect('store')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                usertest = Accounts.objects.get(username=user)
                print(usertest)
                return redirect('login')

        context = {'form':form,'cartItems': cartItems}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    data = cartData(request)
    cartItems = data['cartItems']
    if request.user.is_authenticated:
        return redirect('store')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('store')
            else:
                messages.info(request, 'Username OR Password is incorrect')
                render(request, 'accounts/login.html')
        context = {'cartItems': cartItems}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    contex = {'products':products, 'cartItems': cartItems}
    return render(request, 'store.html', contex)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    contex = {'items':items, 'order' :order, 'cartItems':cartItems}
    return render(request, 'cart.html', contex)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    contex = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'checkout.html', contex)


def updateItem(request):
    data = json.loads(request.body)
    size = int(data['size'])
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('ProductId:', productId)
    print('Size and type:', size)
    print(type(size))

    user = request.user

    customer = Customer.check_user(user)
    product = Product.objects.get(id=productId)
    product.size = size
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product, size = size)
    print(orderItem)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
  
    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        user = request.user

        customer = Customer.check_user(user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )
    return JsonResponse('Payment Complete!', safe=False)

def terms(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'terms.html', context)

def about(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'about.html', context)



