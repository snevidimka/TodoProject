from django.urls import path
from main.views import main_view, edit_view


app_name = 'main'

urlpatterns = [
    path('', main_view, name='main'),
    path('edit/<int:pk>', edit_view, name='edit'),
]

