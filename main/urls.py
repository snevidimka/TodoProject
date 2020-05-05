from django.urls import path
from main.views import main_view, edit_view, create_view, logout_view
from list_item.views import list_item_view


app_name = 'main'

urlpatterns = [
    path('', main_view, name='main'),
    path('edit/<int:pk>', edit_view, name='edit'),
    path('create/', create_view, name='create'),
    path('logout/', logout_view, name='logout'),
]

