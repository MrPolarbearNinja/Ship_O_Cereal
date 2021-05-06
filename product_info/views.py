from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'product_info/Item_Detail.html')


# Create your views here.
