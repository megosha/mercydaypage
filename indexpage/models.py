from django.db import models


# Create your models here.

class Block(models.Model):
    title = models.TextField(verbose_name="Заголовок (блока)", default='', blank=True, null=True)
    subtitle = models.TextField(verbose_name="Подзаголовок", default='', blank=True, null=True)
    content = models.TextField(verbose_name="Основной текст", default='', blank=True, null=True)
    picture = models.TextField(verbose_name="Фоновое изображение", default='', blank=True, null=True)
    item = models.ManyToManyField('Item', verbose_name="Элемент (списка, картинка)", blank=True)
    #title = models.TextField(verbose_name="Заголовок (h1)", default='', blank=True, null=True)

    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"


class Item(models.Model):
    order = models.SmallIntegerField(verbose_name="Порядок отображения", default=0, blank=True, null=True)
    picture = models.FileField(verbose_name="Картинка/фото", default='', blank=True, null=True)
    title = models.TextField(verbose_name="Заголовок (элемента)", default='', blank=True, null=True)
    content = models.TextField(verbose_name="Основной текст", default='', blank=True, null=True)

    class Meta:
        verbose_name = "Элемент"
        verbose_name_plural = "Элементы"


class Settings(models.Model):
    metadescr = models.TextField(verbose_name="Meta Description", default='', blank=True, null=True)
    metakeywords = models.TextField(verbose_name="Meta Keyword", default='', blank=True, null=True)
    title = models.CharField(max_length=32, verbose_name="Заголовок вкладки", default='', blank=True, null=True)

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"
