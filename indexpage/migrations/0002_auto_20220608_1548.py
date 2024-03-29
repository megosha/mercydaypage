# Generated by Django 2.2.12 on 2022-06-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField(blank=True, default=10, null=True, verbose_name='Порядок отображения')),
                ('question', models.TextField(default='', verbose_name='Вопрос')),
                ('answer', models.TextField(blank=True, default='', null=True, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField(blank=True, default=10, null=True, verbose_name='Порядок отображения')),
                ('photo', models.FileField(blank=True, null=True, upload_to='images/gallery', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галерея',
            },
        ),
        migrations.AddField(
            model_name='settings',
            name='about_photo',
            field=models.FileField(blank=True, null=True, upload_to='images/about', verbose_name='Фото о проекте'),
        ),
        migrations.AddField(
            model_name='settings',
            name='about_text',
            field=models.TextField(blank=True, default='В рамках проекта людям, попавшим в трудную жизненную ситуацию и малоимущим семьям раздаются продуктовые пакеты. Каждый участник может бесплатно подобрать для себя одежду, а также получить консультацию психолога, консультацию для нарко- и алкозависимых людей.', null=True, verbose_name='О проекте'),
        ),
        migrations.AddField(
            model_name='settings',
            name='address',
            field=models.CharField(blank=True, default='пр. Комсомольский, 80, 2 этаж, Большой зал', max_length=128, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='settings',
            name='city',
            field=models.CharField(blank=True, default='г. Барнаул', max_length=32, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='settings',
            name='ok',
            field=models.CharField(blank=True, default='https://m.ok.ru/church22ru', max_length=128, null=True, verbose_name='Ссылка на одноклассники'),
        ),
        migrations.AddField(
            model_name='settings',
            name='requisites',
            field=models.TextField(blank=True, default='Местная религиозная организация Церковь Христиан Веры Евангельской (пятидесятников) «Благословение» г. Барнаул, Алтайский край ОГРН: 1112202000800 ИНН: 2223995025 КПП: 222501001', null=True, verbose_name='Реквизиты'),
        ),
        migrations.AddField(
            model_name='settings',
            name='tg',
            field=models.CharField(blank=True, default='https://t.me/church22ru', max_length=128, null=True, verbose_name='Ссылка на Telegram'),
        ),
        migrations.AddField(
            model_name='settings',
            name='vk',
            field=models.CharField(blank=True, default='https://vk.com/church22ru', max_length=128, null=True, verbose_name='Ссылка на Вконтакте'),
        ),
    ]
