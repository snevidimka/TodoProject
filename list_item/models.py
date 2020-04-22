# from django.db import models
#
#
# class ListItemModel(models.Model):
#     """ Модель пунктов списка """
#     name = models.CharField(max_length=128, verbose_name='Пункты списка')
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
#     listmodel_id = models.ForeignKey('main.ListModel', on_delete=models.CASCADE)
#     is_done = models.BooleanField(default=False)
#     expare_date = models.DateTimeField()
#
#     # def __str__(self):
#     #     return self.name
#
#     class Meta:
#         verbose_name = 'Пункты списка'