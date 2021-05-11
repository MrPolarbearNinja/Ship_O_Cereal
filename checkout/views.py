from django.shortcuts import render, redirect
from checkout.forms.checkout_form import Purchase_Histoyry_Form
from basket.models import Basket
from checkout.models import Checkout

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Purchase_Histoyry_Form(data=request.POST)
        if form.is_valid():
            task = form.save()
            make_checkout(request, task.id)
            return redirect('index')
    return render(request, 'checkout/checkout.html', {
        'form': Purchase_Histoyry_Form()
    })

def make_checkout(request, purches_id):
    basket = Basket.objects.filter(user_id=request.user.id)
    basket = Basket.objects.filter(user_id=request.user.id)
    for row in basket:
        check = Checkout(purchase_id=purches_id, items_id=row.item_id, user_id=request.user.id)
        check.save()

