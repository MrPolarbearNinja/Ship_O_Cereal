from django.shortcuts import render
from product_info.models import Items
from history.models import History
from django.http import JsonResponse


# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        context = {'Items': Items.objects.filter(name__contains=search_filter)}
    if 'search_type' in request.GET:
        search_type = request.GET['search_type']
        context = {'Items': Items.objects.filter(type=search_type)}
    else:
        context = {'Items' : Items.objects.all().order_by('id'), 'History': History.objects.all().filter(user=request.user.id).order_by('-time')[0:3]}
    return render(request, 'catalogue/catalogue.html', context)