import pytest
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.common.by import By
from django.db import connections
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from list_item.models import ListItemModel
from main.models import ListModel


TEST_CLIENT = {
    'username': 'TestUser',
    'email': '123@123.ru',
    'password': 'q1w2e3r4TT',
}


@pytest.fixture
def new_client(db):
    new_client = User(
        username=TEST_CLIENT['username'],
        email=TEST_CLIENT['email'],
    )
    new_client.set_password(TEST_CLIENT['password'])
    new_client.save()
    return new_client


@pytest.fixture
def new_list(new_client):
    list_ = ListModel(
        name='Тестовый список дел',
        user=new_client
    )
    list_.save()
    return list_


@pytest.fixture
def new_list_item(new_list):
    list_item = ListItemModel(
        list=new_list,
        name='Тестовое дело',
        expare_date='2020-05-23'
    )
    list_item.save()
    return list_item