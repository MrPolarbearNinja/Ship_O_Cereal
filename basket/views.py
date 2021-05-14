from django.shortcuts import render, redirect
from basket.models import Basket
from product_info.models import Item_Stock

def basket(request):
    if request.method == 'POST':
        print(1)
        print(request.user.id)
        print(request.POST)

    total = 0
    basket = Basket.objects.all().filter(user=request.user.id)
    for item in basket:
        total += item.item.price

    return render(request, 'basket/basket.html', {
        'basket': Basket.objects.all().filter(user=request.user.id),
        'total': total
    })

def delete_from_basket(request, id):
    if Basket.objects.filter(user_id=request.user.id, id=id):
        instance = Basket.objects.get(id=id)
        instance.delete()
        item = Item_Stock.objects.get(id=instance.item_id)
        item.quantity += instance.quantity
        item.save()
    return redirect('basket')
