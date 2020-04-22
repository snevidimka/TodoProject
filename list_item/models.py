from django.db import models


class ListItemModel(models.Model):
    """ Модель элемента списка """
    name = models.CharField(max_length=128, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    list = models.ForeignKey('main.ListModel', on_delete=models.CASCADE, verbose_name='Список дел')
    is_done = models.BooleanField(default=False)
    expare_date = models.DateField(blank=True, null=True)

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = 'Элемент списка'