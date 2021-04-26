from django.db import models

# Create your models here.

class MyGoods(models.Model):
    title=models.CharField(verbose_name='Наименование товара',max_length=255)

    created_at = models.DateTimeField(
        verbose_name=u'Дата добавления',
        auto_created=True,
        auto_now_add=True
     )
    modifed_at=models.DateTimeField(verbose_name=u'Дата изменения')

    price=models.IntegerField(verbose_name='Цена')

    vendor = models.TextField(verbose_name='Поставщик')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Карточка товара'
        verbose_name_plural='Карточки товаров'
