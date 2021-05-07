from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'account_info/account_info.html')