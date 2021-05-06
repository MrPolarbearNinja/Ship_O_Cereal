from django.shortcuts import render, get_object_or_404
from product_info.models import Items


# Create your views here.
def index(request):
    context = {'Items': Items.objects.all().order_by('name')}
    return render(request, 'catalogue/catalogue.html', context)

def get_item_by_id(request, id):
    return render(request, 'product_info/Item_Detail.html', {
        'item' : get_object_or_404(Items, pk=id)
    })




# Create your views here.
