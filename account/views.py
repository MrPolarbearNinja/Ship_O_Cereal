from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from account.models import User

# Create your views here.
from account.forms.account_form import Account_Create_Form


def index(request):
    form = Account_Create_Form()
    return render(request, 'account_log_in/acount_login.html', {
        'form': form
    })

def create_account(request):
    if request.method == 'POST':
        form = Account_Create_Form(data=request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'account_log_in/acount_login.html')
    else:
        form = Account_Create_Form()
    return render(request, 'account_log_in/acount_login.html', {
        'form': form
    })

def edit_account(request):
    profile = User.objects.filter(user=request.user).first()
    if request.method == 'POST':
        print(1)

    return render(request, 'account_info/account_info.html', {
        'form': ''
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'account_log_in/register.html', {
        'form': UserCreationForm()
    })




