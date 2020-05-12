from django.shortcuts import render, redirect, reverse
from list_item.models import ListItemModel
from main.models import ListModel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from list_item.forms import ListItemForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


PAGE_COUNT = 6


@login_required(login_url='registration/login/')
def list_item_view(request, pk):
    ''' при запросе вернет ответ со страничкой list.html '''

    list_name = ListModel.objects.filter(id=pk, user_id=request.user.id).first()
    if not list_name:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    lists = ListItemModel.objects.filter(list_id=pk).order_by('-created')

    paginator = Paginator(lists, PAGE_COUNT)
    page = request.GET.get('page')

    try:
        list_page = paginator.page(page)
    except PageNotAnInteger:
        list_page = paginator.page(1)
    except EmptyPage:
        list_page = paginator.page(paginator.num_pages)

    context = {
        'lists': list_page,
        'list_name': list_name,
        'pages': list(paginator.page_range),  # общее кол-во страниц
    }
    return render(request, 'list.html', context)



def create_item_view(request, pk):
    """ Создание нового списка дел """
    form = ListItemForm()

    if request.method == 'POST':
        name = request.POST['name']
        expare_date = request.POST['expare_date']
        form = ListItemForm({'name': name, 'expare_date': expare_date, 'list': pk})
        success_url = reverse('list_item:list_item', kwargs={'pk': pk})

        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'new_list_item.html', {'form': form, 'pk': pk})


@login_required(login_url='registration/login/')
def edit_item_view(request, pk):
    """ Редактирование существующего списка дел """
    obj = ListItemModel.objects.filter(id=pk).first()
    form = ListItemForm(instance=obj)

    if request.method == 'POST':
        name = request.POST['name']
        expare_date = request.POST['expare_date']
        form = ListItemForm({'name': name, 'expare_date': expare_date, 'list': pk})
        success_url = reverse('list_item:list_item', kwargs={'pk': pk})

        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'new_list.html', {'form': form})
