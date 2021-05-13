from django.shortcuts import render, redirect
from basket.models import Basket
from product_info.models import Items
# Create your views here.
def index(request):
    if request.method == 'POST':
        print(1)
        print(request.user.id)
        print(request.POST)


    context = {'basket': Basket.objects.all().filter(user=request.user.id)}
    return render(request, 'basket/basket.html', context)

def delete_from_basket(request, id):
    print(1)
    if Basket.objects.filter(user_id=request.user.id, id=id):
        instance = Basket.objects.get(id=id)
        instance.delete()
    else:
        print(no)
    return redirect('index')
