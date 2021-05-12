from django.shortcuts import render
from product_info.models import Items
from history.models import History
from basket.models import Basket


# Create your views here.
def index(request):
    sortby = 'id'
    if 'sort_by_price' in request.GET:
        sortby = 'price'

    if ('search_filter' in request.GET and 'search_type' in request.GET):
        context = {}
        context1 = {'Items': None}
        context2 = {'Items': None}
        if 'search_filter' in request.GET:
            search_filter = request.GET['search_filter']
            context1 = {'Items': Items.objects.filter(name__icontains=search_filter)}
        if 'search_type' in request.GET:
            search_type = request.GET['search_type']
            context2 = {'Items': Items.objects.filter(type=search_type)}

        context['Items'] = context1['Items'] & context2['Items']

    elif ('search_filter' in request.GET or 'search_type' in request.GET):
        if 'search_filter' in request.GET:
            search_filter = request.GET['search_filter']
            context = {'Items': Items.objects.filter(name__icontains=search_filter)}
        elif 'search_type' in request.GET:
            search_type = request.GET['search_type']
            context = {'Items': Items.objects.filter(type=search_type)}
        else:
            context = {'Items': Items.objects.all().order_by('id')}

    else:
        context = {'Items': Items.objects.all().order_by('id')}

    context['history'] = History.objects.all().filter(user=request.user.id).order_by('-time')[0:3]
    context['basket'] = Basket.objects.all().filter(user=request.user.id)
    return render(request, 'catalogue/catalogue.html', context)