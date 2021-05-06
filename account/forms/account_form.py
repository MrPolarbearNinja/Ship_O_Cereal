from django.forms import ModelForm, widgets
from account.models import User


class Account_Create_Form(ModelForm):
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.PasswordInput(attrs={'class': 'form-control'})
        }