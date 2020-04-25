from django.shortcuts import render
from list_item.models import ListItemModel
from main.models import ListModel


def list_item_view(request, pk):
    '''при запросе вернет ответ со страничкой list.html'''
    lists = ListItemModel.objects.filter(id=pk)
    context = {
        'lists': lists,
    }
    return render(request, 'list.html', context)

