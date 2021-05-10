from django.forms import ModelForm, widgets
from history.models import History


class History_create(ModelForm):
    class Meta:
        model = History
        widgets = {
            'id': {{item.id}},
            'date': '20:20',
            'user_id': {{user.id}}
        }