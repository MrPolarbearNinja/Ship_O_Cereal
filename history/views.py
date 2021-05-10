from django.shortcuts import render
from history.models import History


def index(request):
    context = {'History': History.objects.all()}
    return render(request, 'history_bar.html', context)