from django.shortcuts import render, redirect
from checkout.forms.checkout_form import Purchase_Histoyry_Form
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Purchase_Histoyry_Form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'checkout/checkout.html', {
        'form': Purchase_Histoyry_Form()
    })
