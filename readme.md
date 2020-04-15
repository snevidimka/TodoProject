# DataBases
- какие БД поддерживает джанго
- почему постгрес
- pip install psycop2
- makemigrations
- migrate
- создание суперпользователя
- служебные таблицы

# Templates

## Homeworks
- повторить операциис БД, все должно работать
- создать новое приложение (app)
django-admin startapp list_item
- создать папку template для этого приложения
- в папке сделать новый шаблон list.html
- к нему написать аналогичную views.py для нового списка
- прописать новый url в urls.py
- прописать в settings.py наше приложение
- заполнить данными из словаря аналогично первыми
- добавить стиль для вычеркивания (добавить стиль css is_done)

пример:
data = {
    'list': [
        {'name': 'Работа', 'is_done': Trueб 'date' = },
        {'name': 'Дом', 'is_done': False},
        {'name': 'Учеба', 'is_done': True}
    ],
    'user_name': 'Admin',
