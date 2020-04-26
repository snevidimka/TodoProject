from django.shortcuts import render, reverse, redirect
from main.models import ListModel
from main.forms import ListForm
from list_item.models import ListItemModel


def main_view(request):
    '''при запросе вернет ответ со страничкой index.html'''
    # ListItem.objects.filter(list__user_username='Admin')
    user = request.user
    lists = ListModel.objects.filter(user=user,).order_by('created')
    context = {
        'lists': lists,
        'user': user.username,
    }
    return render(request, 'index.html', context)


def edit_view(request, pk):
    return


def create_view(request):
    form = ListForm()

    if request.method == 'POST':
        form = ListForm(request.POST)
        success_url = reverse('main:create')

        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'new_list.html', {'form': form})
