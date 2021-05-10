from django.shortcuts import render
from product_info.models import Items
from django.http import JsonResponse


# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        print(search_filter)
        context = {'Items': Items.objects.filter(name__contains=search_filter)}
    else:
        context = {'Items' : Items.objects.all()
            .order_by('id')}
    return render(request, 'catalogue/catalogue.html', context)