from django.shortcuts import render, get_object_or_404
from product_info.models import Items
from django.forms import ModelForm, widgets
from history.models import History
import time

# Create your views here.
def index(request):
    context = {'Items': Items.objects.all().order_by('name')}
    return render(request, 'catalogue/catalogue.html', context)

def get_item_by_id(request, id):
    if request.user.is_authenticated:
        if not History.objects.filter(user_id=request.user.id, item_id=id):
            hist = History(time=time.time(), user_id=request.user.id, item_id=id)
            hist.save()
        else:
            hist_update = History.objects.get(user_id=request.user.id, item_id=id)
            hist_update.time = time.time()
            hist_update.save()


    return render(request, 'product_info/item_detail.html', {
        'item': get_object_or_404(Items, pk=id),
        'History': History.objects.all().filter(user=request.user.id).order_by('-time')[0:3]
    })




# Create your views here.
