from django.shortcuts import render, get_object_or_404
from product_info.models import Items
from django.forms import ModelForm, widgets
from history.models import History
import time

from history.forms.history_form import History_create


# Create your views here.
def index(request):
    context = {'Items': Items.objects.all().order_by('name')}
    return render(request, 'catalogue/catalogue.html', context)

def get_item_by_id(request, id):
    if request.user.is_authenticated:
        hist = History(time=time.time(), user_id=request.user.id, item_id=id)
        hist.save()

    print(request.user.id)
    print(id)

    return render(request, 'product_info/item_detail.html', {
        'item' : get_object_or_404(Items, pk=id)
    })




# Create your views here.
