from django.forms import ModelForm
from django import forms
from checkout.models import Purchase_History


class Purchase_Histoyry_Form(ModelForm):
    class Meta:
        model = Purchase_History
        exclude = ['id', 'user', 'confirmed', 'card']
