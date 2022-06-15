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
    city = models.CharField(max_length=32, verbose_name="Город", default='г. Барнаул', blank=True, null=True)
    address = models.CharField(max_length=128, verbose_name="Адрес", default='пр. Комсомольский, 80, 2 этаж, Большой зал', blank=True, null=True)
    about_text = models.TextField(verbose_name="О проекте", default='В рамках проекта людям, попавшим в трудную жизненную ситуацию и малоимущим семьям раздаются продуктовые пакеты. Каждый участник может бесплатно подобрать для себя одежду, а также получить консультацию психолога, консультацию для нарко- и алкозависимых людей.', blank=True, null=True)
    about_photo = models.FileField(upload_to='images/about', verbose_name="Фото о проекте", blank=True, null=True)
    requisites = models.TextField(verbose_name="Реквизиты",
                                  default='Местная религиозная организация Церковь Христиан Веры Евангельской '
                                          '(пятидесятников) «Благословение» г. Барнаул, Алтайский край '
                                          '\nОГРН: 1112202000800 ИНН: 2223995025 КПП: 222501001',
                                  blank=True, null=True)
    map = models.TextField(verbose_name="Код карты",
                           default='<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3A113fbee5d8cac314649ce7156155a694d81b21bea2dc918f36e1f484c6eb3d54&amp;width=100%25&amp;height=400&amp;lang=ru_RU&amp;scroll=true"></script>',
                           blank=True, null=True)
    footer = models.TextField(verbose_name="Текст футера, копирайт", default='<p>© Разработка сайта. Есина М.В., 2022 <a href="https://diceshard.ru" target="_blank">diceshard.ru</a></p>', blank=True, null=True)
    tg = models.CharField(max_length=128, verbose_name="Ссылка на Telegram", default='https://t.me/church22ru', blank=True, null=True)
    vk = models.CharField(max_length=128, verbose_name="Ссылка на Вконтакте", default='https://vk.com/church22ru', blank=True, null=True)
    ok = models.CharField(max_length=128, verbose_name="Ссылка на одноклассники", default='https://m.ok.ru/church22ru', blank=True, null=True)
    registry = models.BooleanField(default=False, verbose_name="Реестр месяца отправлен")

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"

class Gallery(models.Model):
    order = models.SmallIntegerField(verbose_name="Порядок отображения", default=10, blank=True, null=True)
    photo = models.FileField(upload_to='images/gallery', verbose_name="Фото", blank=True, null=True)

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"

class Faq(models.Model):
    order = models.SmallIntegerField(verbose_name="Порядок отображения", default=10, blank=True, null=True)
    question = models.TextField(verbose_name="Вопрос", default='',)
    answer = models.TextField(verbose_name="Ответ", default='', blank=True, null=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"

    def __str__(self):
        return f"№: {self.order}, {self.question}"