from django.shortcuts import render
from product_info.models import Items
from history.models import History
from basket.models import Basket


# Create your views here.
def index(request):
    # The catalogue, with search handling
    sort_by = 'id'
    # The default sort by is id, if there is a request for other sort_by, it will be changed to that
    if 'sort_by_price' in request.GET:
        if request.GET['sort_by_price'] == "1":
            sort_by = 'price'
        elif request.GET['sort_by_price'] == "0":
            sort_by = '-price'
    elif 'sort_by_name' in request.GET:
        if request.GET['sort_by_name'] == "1":
            sort_by = 'name'
        elif request.GET['sort_by_name'] == "0":
            sort_by = '-name'

    # Search by name and type handling
    # First checks if we are searching with both name and type
    if ('search_filter' in request.GET and 'search_type' in request.GET):
        context = {}
        context1 = {'Items': None}
        context2 = {'Items': None}
        if 'search_filter' in request.GET:
            search_filter = request.GET['search_filter']
            context1 = {'Items': Items.objects.filter(name__icontains=search_filter).order_by(sort_by)}
        if 'search_type' in request.GET:
            search_type = request.GET['search_type']
            context2 = {'Items': Items.objects.filter(type=search_type).order_by(sort_by)}

        # Merge together the name and type search
        context['Items'] = context1['Items'] & context2['Items']

    # Here we check if it is ether type or name
    elif ('search_filter' in request.GET or 'search_type' in request.GET):
        if 'search_filter' in request.GET:
            search_filter = request.GET['search_filter']
            context = {'Items': Items.objects.filter(name__icontains=search_filter).order_by(sort_by)}
        elif 'search_type' in request.GET:
            search_type = request.GET['search_type']
            context = {'Items': Items.objects.filter(type=search_type).order_by(sort_by)}
        else:
            context = {'Items': Items.objects.all().order_by('id').order_by(sort_by)}

    # Here, if it is neither name or type
    else:
        context = {'Items': Items.objects.all().order_by('id').order_by(sort_by)}

    curent_basket = Basket.objects.all().filter(user=request.user.id)
    bask_total = 0
    for bitem in curent_basket:
        bask_total += bitem.quantity

    context['history'] = History.objects.all().filter(user=request.user.id).order_by('-time')[0:3]
    context['basket'] = curent_basket
    context['bask_total'] = bask_total
    return render(request, 'catalogue/catalogue.html', context)