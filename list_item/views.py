from django.shortcuts import render
from list_item.models import ListItemModel
from main.models import ListModel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound


@login_required(login_url='/registration/login/')
def list_item_view(request, pk):
    '''при запросе вернет ответ со страничкой list.html'''

    list_name = ListModel.objects.filter(id=pk).first()
    b = list(ListModel.objects.filter(user_id=request.user.pk))
    if b.count(list_name) == 0:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    lists = ListItemModel.objects.filter(list_id=pk)
    context = {
        'lists': lists,
        'list_name': list_name.name,
    }
    return render(request, 'list.html', context)


# def edit_view(request, pk):
#     pass
#
#
# def create_view(request, pk):
#     pass
