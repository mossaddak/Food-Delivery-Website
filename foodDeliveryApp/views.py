from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import (
    FoodMenu,
    PurchasedItem,
    FoodCategories
)
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
from userProfileApp.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect

#for payment
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def error_404_view(request, exception):
    return render(request,'404.html')
 
def Home(request):
    foodMenu = FoodMenu.objects.all()
    context = {
        "foodMenu":foodMenu 
    }
    return render(request, 'index.html', context)



def AllFoodItem(request):
    foodMenu = FoodMenu.objects.all()
    context = {
        "foodMenu":foodMenu
    }
    return render(request, 'all_food_items.html', context)


def PageNotFound(request):
    context = {

    }
    return render( request, '404.html', context)  

def QuickView(request, pk):
    quickView = get_object_or_404(FoodMenu, pk=pk)
    context = {
        "foodDetails":quickView,
    } 
    return render(request, 'quickView.html', context)

@login_required(login_url='Login')  
def OrderItem(request,pk):
    quickView = get_object_or_404(FoodMenu, pk=pk)
 
    context = {
        "foodDetails":quickView,
    }

    return render(request, 'orderItem.html', context)

@login_required(login_url='Login')  
def MakePayment(request,pk):

    #secrete keys
    store_id = 'mossa637cf3a049a0e'
    API_key = 'mossa637cf3a049a0e@ssl'
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_key)


    #url
    status_url = request.build_absolute_uri(reverse('PaymentStatus'))
    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url    )


    #product information
    orderItem = get_object_or_404(FoodMenu, pk=pk)
    orderQTY = request.POST.get('order_qty')
    itemPrice = orderItem.Price
    order_total = int(orderQTY)*int(itemPrice)

    mypayment.set_product_integration(
        total_amount=Decimal(order_total),
        currency='BDT',
        product_category='Mixed',
        product_name=orderItem,
        num_of_item=orderQTY,
        shipping_method='Courier',
        product_profile='None'
    )

    #sender info
    mypayment.set_customer_info(
        name=request.user.first_name,
        email=request.user.email,
        address1=request.user.address,
        address2=request.user.address,
        city=request.user.district,
        postcode=request.user.zipcode,
        country='Bangladesh',
        phone = request.user.phone_number
    )

    #billing info
    mypayment.set_shipping_info(
        shipping_to=request.user.first_name,
        address=request.user.address,
        city=request.user.district,
        postcode=request.user.zipcode,
        country='Bangladesh'
    )
    response_data = mypayment.init_payment()

    if request.method == "POST":
        PurchasedItem.objects.create(
            user = request.user,
            customerName = request.POST.get('full_name'),
            item=orderItem,
            itemPrice=itemPrice,
            quantity=orderQTY,
            totalPrice=order_total, 
            phone_number=request.POST.get('phone_number'),
            post_office=request.POST.get('post_office'),
            thana=request.POST.get('thana'),
            district=request.POST.get('district'),
            zipcode=request.POST.get('zipcode'),
            address=request.POST.get('address'), 
        )

    return redirect(response_data['GatewayPageURL'])


@csrf_exempt
def PaymentStatus(request):
    
    if request.method == 'POST' or request.method == 'post': 
        payment_data = request.POST
        status = payment_data['status']
        

        if status == 'VALID':

            tran_id = payment_data['tran_id']
            val_id = payment_data['val_id']

            messages.info(request,"Your payment successfully done.")
            return HttpResponseRedirect(reverse("PurchasedProduct", kwargs={'tran_id':tran_id, 'val_id':val_id}))
            
        elif status == 'FAILED':
            messages.warning(request,"Your payment failed. Please try again.")
        elif status == 'error':
            messages.warning(request,"Insufficient balance. Please try again.")

    context = {

    }
    return render(request, 'payment_status.html', context)  


@login_required(login_url='Login')
def PurchasedProduct(request,tran_id,val_id):

    
    

    context = {
        
    }
    return render(request, 'purchased-products.html', context)