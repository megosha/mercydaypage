from django.db import models


# Create your models here.

class Block(models.Model):
    order = models.SmallIntegerField(verbose_name="Порядок отображения", default=0, blank=True, null=True, unique=True)
    title = models.TextField(verbose_name="Заголовок (блока)", default='', blank=True, null=True)
    subtitle = models.CharField(max_length=255, verbose_name="Подзаголовок", default='', blank=True, null=True)
    content = models.TextField(verbose_name="Основной текст", default='', blank=True, null=True)
    picture = models.FileField(verbose_name="Фоновое изображение", default='', blank=True, null=True)
    item = models.ManyToManyField('Item', verbose_name="Элемент (списка, картинка)", blank=True)
    # pic = models.ImageField(upload_to='static/images/', verbose_name="Фоновое изображение2", default='', blank=True, null=True)

    def __str__(self):
        return f"№: {self.order}, Имя: {self.title}"

    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"
        #unique_together = (('item', 'item__order'),)


class Item(models.Model):
    order = models.SmallIntegerField(verbose_name="Порядок отображения", default=0, blank=True, null=True)
    picture = models.FileField(verbose_name="Картинка/фото", default='', blank=True, null=True)
    title = models.TextField(verbose_name="Заголовок (элемента)", default='', blank=True, null=True)
    content = models.TextField(verbose_name="Основной текст", default='', blank=True, null=True)

    def __str__(self):
        return f"№: {self.order}, Имя: {self.title}"

    class Meta:
        verbose_name = "Элемент"
        verbose_name_plural = "Элементы"


class Settings(models.Model):
    metadescr = models.TextField(verbose_name="Meta Description", default='', blank=True, null=True)
    metakeywords = models.TextField(verbose_name="Meta Keyword", default='', blank=True, null=True)
    title = models.CharField(max_length=32, verbose_name="Заголовок вкладки", default='', blank=True, null=True)
    phone = models.CharField(max_length=32, verbose_name="ТЕлефон для всех мест на сайте", default='', blank=True, null=True)
    email = models.EmailField(verbose_name="Email для рассылки заявок", default='', blank=True, null=True)
    date = models.DateTimeField(default=None, verbose_name="Дата и время проведения", blank=True, null=True)
    registry = models.BooleanField(default=False, verbose_name="Реестр месяца отправлен")

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"
