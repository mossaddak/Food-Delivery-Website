from django.shortcuts import render,redirect,get_object_or_404
from .models import (
    BilligAddress
)
from .forms import BillingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from foodDeliveryApp.models import FoodMenu

# Create your views here.
@login_required
def Checkout(request):
    saved_address = BilligAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = BillingForm(instance=saved_address)

    if request.method=="POST":
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            messages.success(request, "Billing address saved.")
            redirect('Checkout')
        else:
            messages.success(request, "Try to submit again.")
            redirect('Checkout')
    else:
        messages.success(request, "Try to submit again.")
        redirect('Checkout')
    context = {
        "saved_address":saved_address,
        "form":form,
    }

    return render(request, 'checkout.html', context) 







  