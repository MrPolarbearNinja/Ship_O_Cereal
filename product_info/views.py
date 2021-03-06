from django.shortcuts import render, get_object_or_404
from product_info.models import Items
from django.shortcuts import redirect
from history.models import History
from basket.models import Basket
from product_info.models import Item_Stock
import time


# Create your views here.
def index(request):
    # If you get here, you are at the wrong place, but will send you to the main page
    return redirect('/')


def get_item_by_id(request, id):
    # To see a specific item, we go through here
    if request.user.is_authenticated:
        # If the user is lodged in, we add the browsed item to the user browsing history
        if not History.objects.filter(user_id=request.user.id, item_id=id):
            hist = History(time=time.time(), user_id=request.user.id, item_id=id)
            hist.save()
        # If it is already in the history, we only need to update the timer
        else:
            hist_update = History.objects.get(user_id=request.user.id, item_id=id)
            hist_update.time = time.time()
            hist_update.save()

    bask_total = 0
    curent_basket = Basket.objects.all().filter(user=request.user.id)
    for bitem in curent_basket:
        bask_total += bitem.quantity

    return render(request, 'product_info/item_detail.html', {
        'item': get_object_or_404(Items, pk=id),
        'history': History.objects.all().filter(user=request.user.id).order_by('-time')[0:3],
        'basket': curent_basket,
        'bask_total': bask_total
    })


def add_to_basket(request, id, qty):
    item_stock = Item_Stock.objects.get(item_id=id)
    # Checks if there is available stock for this product
    if (item_stock.quantity > 0):
        if not Basket.objects.filter(user_id=request.user.id, item_id=id):
            Bask = Basket(quantity=qty, user_id=request.user.id, item_id=id)
            Bask.save()
        else:
            Bask_update = Basket.objects.get(user_id=request.user.id, item_id=id)
            Bask_update.quantity = Bask_update.quantity + qty
            Bask_update.save()
        # Removes from the stock
        item_stock.quantity -= qty
        item_stock.save()

    return redirect('/product-info/' + str(id))