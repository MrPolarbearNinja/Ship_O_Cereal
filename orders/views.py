from django.shortcuts import render
from checkout.models import Purchase_History


def orders(request):
    success = False
    #Only to display the success massage
    if 'success' in request.GET:
        success = True

    return render(request, 'orders/orders.html', {
        'orders': Purchase_History.objects.filter(user_id=request.user.id).order_by('-id'),
        'success': success
    })