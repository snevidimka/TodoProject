# from django import template
# from django.utils.html import format_html
from django.template.defaulttags import register
from TodoProject.settings import DIV_COUNT


@register.filter
def get_count(lists):
    """
    Возвращает список - количество, для генераци пустых блоков
    """

    return list(range(DIV_COUNT - len(lists)))

# @register.filter
# def my_tag(lists):
#     result = ''
#     for i in range(DIV_COUNT - len(lists)):
#         result += '<div class="table-data__table-row"></div>'
#     return format_html(result)

