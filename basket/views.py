from django.shortcuts import render
from basket.models import Basket
from product_info.models import Items
# Create your views here.
def index(request):
    context = {'basket': Basket.objects.all().filter(user=request.user.id)}
    return render(request, 'basket/basket.html', context)