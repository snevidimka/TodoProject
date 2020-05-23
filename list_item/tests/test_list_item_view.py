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
def test_create_item_view(new_client, new_list, new_list_item):
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

