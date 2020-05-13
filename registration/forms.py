from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS


class CustomUserForm(UserCreationForm):
    """ Форма регистрации нового пользователя """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Имя уже существует",
            }
        }


class LoginForm(forms.Form):
    login = forms.CharField(required=True, max_length=64, widget=forms.TextInput())
    password = forms.CharField(required=True, max_length=64, widget=forms.PasswordInput())

