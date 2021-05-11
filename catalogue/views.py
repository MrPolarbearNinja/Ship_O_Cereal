from django.shortcuts import render
from product_info.models import Items
from history.models import History
from django.http import JsonResponse


# Create your views here.
def index(request):
    if (len(request.GET) == 2):
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
    elif len(request.GET) == 1:
        if 'search_filter' in request.GET:
            search_filter = request.GET['search_filter']
            context = {'Items': Items.objects.filter(name__icontains=search_filter)}
        elif 'search_type' in request.GET:
            search_type = request.GET['search_type']
            context = {'Items': Items.objects.filter(type=search_type)}

    else:
        context = {'Items' : Items.objects.all().order_by('id')}
    context['History'] = History.objects.all().filter(user=request.user.id).order_by('-time')[0:3]
    return render(request, 'catalogue/catalogue.html', context)