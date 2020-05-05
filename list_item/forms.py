from django import forms
from list_item.models import ListItemModel
from django.core.exceptions import NON_FIELD_ERRORS


class ListItemForm(forms.ModelForm):
    """ Форма настроек расписания обмена """
    name = forms.CharField(required=True, widget=forms.TextInput())
    expire_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ListItemModel
        fields = ('name', 'expire_date', 'list')
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Имя уже существует",
            }
        }
