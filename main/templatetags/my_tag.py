from django import template
from django.utils.html import format_html

register = template.Library()


@register.filter()
def my_tag(value):
    result = ''
    count = 6 - len(value)
    for i in range(count):
        result += '<div class="table-data__table-row"></div>'
    return format_html(result)
