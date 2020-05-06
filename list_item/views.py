from django.shortcuts import render, redirect, reverse
from list_item.models import ListItemModel
from main.models import ListModel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from list_item.forms import ListItemForm
from django.contrib.auth import logout


@login_required(login_url='registration/login/')
def list_item_view(request, pk):
    ''' при запросе вернет ответ со страничкой list.html '''

    list_name = ListModel.objects.filter(id=pk, user_id=request.user.id).first()
    if not list_name:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    lists = ListItemModel.objects.filter(list_id=pk)
    context = {
        'lists': lists,
        'list_name': list_name,
    }
    return render(request, 'list.html', context)


@login_required(login_url='registration/login/')
def create_item_view(request, pk):
    form = ListItemForm()

    if request.method == 'POST':
        name = request.POST['name']
        expare_date = request.POST['expare_date']
        form = ListItemForm({'name': name, 'expare_date': expare_date, 'list': pk})
        success_url = reverse('list_item:list_item', kwargs={'pk': 5})

        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'new_list_item.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('main:main')


def edit_item_view(request, pk):
    obj = ListItemModel.objects.filter(id=pk).first()
    form = ListItemForm(instance=obj)

    if request.method == 'POST':
        name = request.POST['name']
        expare_date = request.POST['expare_date']
        form = ListItemForm({'name': name, 'expare_date': expare_date, 'list': pk})
        success_url = reverse('list_item:list_item', kwargs={'pk': 5})

        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'new_list.html', {'form': form})
