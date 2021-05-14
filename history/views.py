from django.shortcuts import render
from history.models import History


def index(request):
    # The view for the history side bar
    context = {'History': History.objects.all()}
    return render(request, 'history_bar.html', context)