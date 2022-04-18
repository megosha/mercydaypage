import os
from time import sleep
from datetime import datetime

from django.conf import settings as sts
from django.core.management.base import BaseCommand
from django.core.mail.message import EmailMultiAlternatives

from indexpage import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        sleep_time = 18000
        settings = models.Settings.objects.get()

        while True:
            if settings.date is None and settings.registry:
                settings.registry = False
                settings.save()


            if settings.date is not None and settings.date.date() == datetime.now().date() and not settings.registry:
                date_time = settings.date.strftime("%m.%d.%Y")
                subject = f'Реестр заявок на проект "День Милосердия" {date_time}'
                message = f''
                email = settings.email

                filename = os.path.join(sts.BASE_DIR, f'{settings.date.date()}.xls')

                mail = EmailMultiAlternatives(subject, message, sts.DEFAULT_FROM_EMAIL, (email,))
                mail.attach_file(os.path.join(filename))
                try:
                    mail.send(fail_silently=False)
                    settings.registry = True
                    settings.save()
                except Exception as e:
                    print(e)

            sleep(sleep_time)













