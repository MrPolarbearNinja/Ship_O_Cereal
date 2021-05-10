from django.shortcuts import render
from product_info.models import Items
from django.http import JsonResponse


# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        items = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'type_id': x.type_id,
            'image': x.items_image_set.first().image_link
        } for x in Items.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': items})
    context = {'Items' : Items.objects.all().order_by('id')}
    return render(request, 'catalogue/catalogue.html', context)