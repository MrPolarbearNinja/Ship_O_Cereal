from django.shortcuts import render, redirect
from checkout.forms.checkout_form import Purchase_Histoyry_Form
from basket.models import Basket
from checkout.models import Checkout
from checkout.models import Purchase_History
from django.urls import reverse

# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.method == 'POST':
            form = Purchase_Histoyry_Form(data=request.POST)
            if form.is_valid():
                task = form.save()
                make_checkout(request, task.id)
        return redirect('review')
    return render(request, 'checkout/checkout.html', {
        'form': Purchase_Histoyry_Form()
    })

def make_purchase(request):
    if request.method == 'POST':
        last_purches = Purchase_History.objects.filter(user_id=request.user.id).order_by('-id').first()
        last_purches.confirmed = True
        last_purches.save()
        make_checkout(request, last_purches.id)
        empty_basket(request)
        return redirect('/')
    return render(request, 'checkout/review.html')

def make_checkout(request, purches_id):
    basket = Basket.objects.filter(user_id=request.user.id)
    for row in basket:
        check = Checkout(purchase_id=purches_id, items_id=row.item_id, user_id=request.user.id)
        check.save()

def empty_basket(request):
    Basket.objects.filter(user_id=request.user.id).delete()
