from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from account.forms.account_form import Account_Create_Form


def index(request):
    return render(request, 'account_log_in/acount_login.html')

def create_account(request):
    if request.method == 'POST':
        print(1)
    else:
        form = Account_Create_Form
    return render(request, 'account_log_in/sign_up_form.html', {
        'form' : form
    })