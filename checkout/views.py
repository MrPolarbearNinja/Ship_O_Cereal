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
                task = form.save(commit=False)
                task.user_id = request.user.id
                task.save()
                make_checkout(request, task.id)
                empty_basket(request)
        return redirect('review', task.id)
    return render(request, 'checkout/checkout.html', {
        'form': Purchase_Histoyry_Form()
    })

def make_purchase(request, id):
    purches = Purchase_History.objects.get(id=id)
    #makes sure the person that is logged in is reviewing his own purches
    if (purches.user_id != request.user.id):
        return redirect('/')

    if request.method == 'POST':
        purches.confirmed = True
        purches.save()
        return redirect('/')
    return render(request, 'checkout/review.html', {
        'purches_info': purches,
        'checkout': Checkout.objects.all().filter(user=request.user.id, purchase_id=id)
    })

def make_checkout(request, purches_id):
    basket = Basket.objects.filter(user_id=request.user.id)
    for row in basket:
        check = Checkout(purchase_id=purches_id, items_id=row.item_id, user_id=request.user.id)
        check.save()

def empty_basket(request):
    Basket.objects.filter(user_id=request.user.id).delete()
