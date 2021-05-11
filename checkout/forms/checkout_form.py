from django.forms import ModelForm, widgets
from checkout.models import Purchase_History


class Purchase_Histoyry_Form(ModelForm):
    class Meta:
        model = Purchase_History
        exclude = ['id']