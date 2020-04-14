from django.shortcuts import render

# Create your views here.

def main_view(request):
    '''при запросе вернет ответ со страничкой index.html'''
    return render(request, 'index.html')
