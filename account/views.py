from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from account.forms.profile_form import Profile_Form
from account.models import User
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

def Profile(request):
    profile = User.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = Profile_Form(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'account_info/account_info.html', {
        'form': Profile_Form()
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




