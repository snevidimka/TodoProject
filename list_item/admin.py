from django.contrib import admin
from list_item.models import ListItemModel


class ListAdmin(admin.ModelAdmin):

    list_display = ['id', 'created', 'name', 'is_done', 'list']
    list_filter = ['created', 'name', 'is_done', 'list']
    search_fields = ['name', 'list']


admin.site.register(ListItemModel, ListAdmin)

