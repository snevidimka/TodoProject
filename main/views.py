from django.shortcuts import render

# Create your views here.


data = {
    'lists': [
        {'name': 'Работа', 'is_done': True},
        {'name': 'Дом', 'is_done': False},
        {'name': 'Учеба', 'is_done': True}
    ],
    'user_name': 'Admin',
}


def main_view(request):
    '''при запросе вернет ответ со страничкой index.html'''
    context = data
    return render(request, 'index.html', context)
