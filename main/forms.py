from django import forms
from main.models import ListModel


class ListForm(forms.ModelForm):
    """ Форма настроек расписания обмена """
    name = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = ListModel
        fields = ('name',)
