from django.shortcuts import render
from product_info.models import Items


# Create your views here.
def index(request):
    context = {'Items' : Items.objects.all().order_by('name')}
    return render(request, 'catalogue/index.html', context)