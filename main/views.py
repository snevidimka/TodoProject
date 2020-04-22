from django.shortcuts import render
from main.models import ListModel
# from list_item.models import ListItem


def main_view(request):
    '''при запросе вернет ответ со страничкой index.html'''
    # ListItem.objects.filter(list__user_username='Admin')
    user = request.user
    lists = ListModel.objects.filter(user=user).order_by('created')

    context = {
        'lists': lists,
        'user': request.user
    }
    return render(request, 'index.html', context)


def edit_view(request, pk):
    return 'Hello'