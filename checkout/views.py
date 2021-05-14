from django.shortcuts import render, redirect
from checkout.forms.checkout_form import Purchase_Histoyry_Form
from basket.models import Basket
from checkout.models import Checkout
from checkout.models import Purchase_History
from django.urls import reverse

# Create your views here.
def index(request):
    # When the the buy button is pressed, we get here to the checkout to write our information
    invalid = False
    # Only to display the invalid massage
    if 'invalid' in request.GET:
        invalid = True

    if request.method == 'POST':
        if request.method == 'POST':
            form = Purchase_Histoyry_Form(data=request.POST)
            if form.is_valid():
                # If the form is valid, a checkout history is made, and a checkout list is also made in the DB
                # Then we go to the review step where th checkout table is used to show item we are about to buy
                task = form.save(commit=False)
                task.user_id = request.user.id
                task.save()
                make_checkout(request, task.id)
                empty_basket(request)
            else:
                return redirect('/checkout/?invalid=true')
        return redirect('review', task.id)
    return render(request, 'checkout/checkout.html', {
        'form': Purchase_Histoyry_Form(),
        'invalid': invalid
    })

def make_purchase(request, id):
    # The review page, where there will be a button to confirm the payment
    purchase = Purchase_History.objects.get(id=id)
    # makes sure the person that is logged in is reviewing his own purchase
    if (purchase.user_id != request.user.id):
        return redirect('/')

    # Here when the confirm button is pressed, and we go to the order history page with a success message
    if request.method == 'POST':
        purchase.confirmed = True
        purchase.save()
        return redirect('/orders/?success=True')

    # Get the totals of the items we are buying
    total = 0
    checkout = Checkout.objects.all().filter(user=request.user.id, purchase_id=id)
    for item in checkout:
        total += item.items.price * item.quantity

    return render(request, 'checkout/review.html', {
        'purches_info': purchase,
        'checkout': checkout,
        'total': total
    })

def make_checkout(request, purches_id):
    # A function to make the checkout row in the DB
    basket = Basket.objects.filter(user_id=request.user.id)
    for row in basket:
        check = Checkout(purchase_id=purches_id, items_id=row.item_id, user_id=request.user.id, quantity=row.quantity)
        check.save()

def empty_basket(request):
    # A function to empty the basket
    Basket.objects.filter(user_id=request.user.id).delete()

