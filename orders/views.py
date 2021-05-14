from django.shortcuts import render
from checkout.models import Purchase_History


def orders(request):
    context = {'orders': Purchase_History.objects.filter(user_id=request.user.id)}
    return render(request, 'orders/orders.html', context)