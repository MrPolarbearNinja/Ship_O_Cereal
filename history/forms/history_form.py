from django.forms import ModelForm, widgets
from history.models import History



class History_create():
    class Meta:
        model = History
        exclude = ['id']
        widgets = {
            'date': 1111,
            'user_id': {{user.id}},
            'item_id': {{item.id}}

        }