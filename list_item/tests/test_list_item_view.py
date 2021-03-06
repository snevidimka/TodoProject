from django.test import Client
from django.shortcuts import reverse
import pytest
from main.forms import ListForm

TEST_CLIENT = {
    'username': 'TestUser',
    'email': '123@123.ru',
    'password': 'q1w2e3r4TT',
}


@pytest.mark.django_db
def test_create_list_item_view(new_client, new_list, new_list_item):
    """
    Проверка вьюхи создание дела
    """
    csrf_client = Client(enforce_csrf_checks=True)
    csrf_client.login(
        username=new_client.username, password=TEST_CLIENT['password']
    )
    csrf_client.get(reverse('list_item:create', kwargs={'pk': new_list.id}))
    csrf = csrf_client.cookies['csrftoken']
    response = csrf_client.post(reverse('list_item:create', kwargs={'pk': new_list.id}), data={
        'name': 'Какое-то дело',
        'csrfmiddlewaretoken': csrf.value,
        'expare_date': '2020-05-23'
    })
    assert response.status_code == 302, response.content.decode()

    response = csrf_client.get(reverse('list_item:list_item', kwargs={'pk': new_list.id}))
    html = response.content.decode('utf8')
    assert 'Какое-то дело' in html


def test_list_item_view(new_client, new_list, new_list_item):
    """
    Проверка что рендерится правильный шаблон страницы list.html
    """
    csrf_client = Client(enforce_csrf_checks=True)
    csrf_client.login(
        username=new_client.username, password=TEST_CLIENT['password']
    )
    response = csrf_client.get(reverse('list_item:list_item', kwargs={'pk': new_list.id}))
    html = response.content.decode('utf8')
    assert response.status_code == 200
    assert '<title>Список</title>' in html
    assert html.strip().endswith('</html>')
    assert 'list.html' in [t.name for t in response.templates]
    assert new_list.name == 'Тестовый список дел'
    assert new_list_item.name == 'Тестовое дело'


@pytest.mark.django_db
def test_delete_list_item_view(new_client, new_list, new_list_item):
    """
    Проверка вьюхи удаление дела
    """
    client = Client(enforce_csrf_checks=False)
    client.login(
        username=new_client.username, password=TEST_CLIENT['password']
    )
    client.get(reverse('list_item:list_item', kwargs={'pk': new_list.id}))
    response = client.post(reverse('list_item:delete', kwargs={'pk': new_list_item.id}), data={
        'list': new_list,
    })
    assert response.status_code == 201, response.content.decode()
    response = client.get(reverse('list_item:delete', kwargs={'pk': new_list.id}))
    assert response.status_code == 404, response.content.decode('utf8')


@pytest.mark.django_db
def test_edit_list_item_view(new_client, new_list, new_list_item):
    """
    Проверка вьюхи редактирование дела
    """
    client = Client(enforce_csrf_checks=False)
    client.login(
        username=new_client.username, password=TEST_CLIENT['password']
    )
    client.get(reverse('list_item:list_item', kwargs={'pk': new_list.id}))
    response = client.post(reverse('list_item:edit', kwargs={'pk': new_list_item.id}), data={
        'name': 'Тестовое дело',
        'expare_date': '2020-05-23'
    })
    assert response.status_code == 302, response.content.decode()
