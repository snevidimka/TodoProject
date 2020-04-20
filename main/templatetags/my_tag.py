from django import template
from django.utils.html import format_html

register = template.Library()


@register.filter()
def my_tag(value):
    result = ''
    for i in range(6 - len(value)):
        result += '<div class="table-data__table-row"></div>'
    return format_html(result)
