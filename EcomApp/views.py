from django.shortcuts import render, HttpResponse
from EcomApp.models import Product, Order
from django.contrib import messages
# Create your views here.
def home(request):
    product = Product.objects.all()
    content = {
        'product' : product
    }
    return render(request,'home.html',content)

def product_page(request,prid):
    one_product = Product.objects.get(id=prid)
    product = Product.objects.all()
    # print(one_product[0])
    content_one = {
        'one_product' : one_product,
        'product' : product
    }
    return render(request,'product_page.html',content_one)

def cart_page(request):
    if request.method == "POST":
        products_ordered = request.POST.get('products_ordered')
        name = request.POST.get('name')
        email_address = request.POST.get('email_address')
        phone_number = request.POST.get('phone_number')
        city = request.POST.get('city')
        country = request.POST.get('country')
        first_address = request.POST.get('first_address')
        second_address = request.POST.get('second_address')
        order = Order(products_ordered=products_ordered, name=name, email_address=email_address,phone_number=phone_number,city=city, country=country,first_address=first_address,second_address=second_address)
        order.save()
        messages.success(request, 'Your Order Has been submited Track Your Order using Order ID: '+ str(order.id))
    return render(request,'cart_page.html')


def tracker(request):
    if request.method=='POST':
        email= request.POST.get('email')
        order_id= request.POST.get('order_id')
        get_det = Order.objects.get(email_address=email, id=order_id)
        messages.success(request, f'The order from "{get_det.name}".\nRegistered Email is "{get_det.email_address}". The states of the order is "{get_det.tracker}": ')
    return render(request, 'tracker.html')


def watches(request):
    product = Product.objects.all().filter(category = 'watches')
    content = {
        'product':product
    }
    return render(request, 'watches.html',content)


def shoes(request):
    product = Product.objects.all().filter(category = 'shoes')
    content = {
        'product':product
    }
    return render(request, 'shoes.html',content)


def mobile_accessories(request):
    product = Product.objects.all().filter(category = 'mobile_accessories')
    content = {
        'product':product
    }
    return render(request, 'mobile_accessories.html',content)


def caps(request):
    product = Product.objects.all().filter(category = 'caps')
    content = {
        'product':product
    }
    return render(request, 'caps.html',content)