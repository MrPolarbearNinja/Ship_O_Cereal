from django.shortcuts import render
from django.http import HttpResponse
from history.models import History
# Create your views here.

def index(request):
    context = {'History': History.objects.all().order_by('id')}
    return render(request, 'history_bar.html', context)