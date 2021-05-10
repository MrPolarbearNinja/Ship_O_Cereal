from django.shortcuts import render
from product_info.models import Items


# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search = request.Get['search_filter']
    context = {'Items' : Items.objects.all().order_by('id')}
    return render(request, 'catalogue/catalogue.html', context)