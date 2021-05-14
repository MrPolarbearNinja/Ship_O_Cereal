from django.shortcuts import render, redirect
from basket.models import Basket
from product_info.models import Item_Stock

def basket(request):
    # The view basket page
    total = 0
    current_basket = Basket.objects.all().filter(user=request.user.id)
    for item in current_basket:
        total += item.item.price * item.quantity

    return render(request, 'basket/basket.html', {
        'basket': Basket.objects.all().filter(user=request.user.id),
        'total': total
    })

def delete_from_basket(request, id):
    # When an item is deleted, it goes through a page with the id of the basket item
    # First, make sure that the basket item id belongs to the user
    if Basket.objects.filter(user_id=request.user.id, id=id):
        instance = Basket.objects.get(id=id)
        instance.delete()
        item = Item_Stock.objects.get(id=instance.item_id)
        item.quantity += instance.quantity
        item.save()
    return redirect('basket')
