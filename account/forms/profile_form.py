from django.forms import ModelForm, widgets
from account.models import User

class Profile_Form(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'user']
        widgets = {
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }