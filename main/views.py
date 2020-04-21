from django.shortcuts import render

# Create your views here.


data = {
    'lists': [
        {'id': 1, 'name': 'Работа', 'is_done': True, 'date': '29.12.2020'},
        {'id': 2, 'name': 'Дом', 'is_done': False, 'date': '30.12.2020'},
        {'id': 3, 'name': 'Учеба', 'is_done': True, 'date': '31.12.2020'}
    ],
    'user_name': 'Admin',
}


def main_view(request):
    '''при запросе вернет ответ со страничкой index.html'''
    context = data
    return render(request, 'index.html', context)


def edit_view(request, pk):

    return 'Hello'