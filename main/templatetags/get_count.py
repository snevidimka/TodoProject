from django import template
from django.utils.html import format_html


register = template.Library()


@register.simple_tag()
def templatetags():
    value = '<div class="table-data__table-row"></div>' \
            '<div class="table-data__table-row"></div>' \
            '<div class="table-data__table-row"></div>'
    return format_html(value)

