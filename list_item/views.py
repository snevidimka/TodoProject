from django.shortcuts import render

# Create your views here.

data = {
    'lists': [
        {'name': 'Купить', 'is_done': True, 'date' : '29.12.2020'},
        {'name': 'Заказать', 'is_done': False, 'date' : '30.12.2020'},
        {'name': 'Разослать', 'is_done': False, 'date' : None}
    ],
    'user_name': 'Admin',
}
def list_item_view(request):
    '''при запросе вернет ответ со страничкой list.html'''
    context = data
    return render(request, 'list.html', context)