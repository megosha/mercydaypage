from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
from indexpage import models, helpers
from django.core.mail import send_mail
from django.conf import settings as sts

from datetime import datetime
import os


# Create your views here.

class Home(View):
    def dispatch(self, request, *args, **kwargs):
        return HttpResponseRedirect('/')


class Index(View):
    def get(self, request):
        navblock = models.Block.objects.get(order=0)
        block1 = models.Block.objects.get(order=1)
        block2 = models.Block.objects.get(order=2)
        block3 = models.Block.objects.get(order=3)
        block4 = models.Block.objects.get(order=4)
        block5 = models.Block.objects.get(order=5)
        block6 = models.Block.objects.get(order=6)
        photo1 = block5.item.filter(order=1).first()
        photo2 = block5.item.filter(order=2).first()
        photo3 = block5.item.filter(order=3).first()
        photo4 = block5.item.filter(order=4).first()
        settings = models.Settings.objects.get()
        datefield = block2.item.filter(order=1).first()
        datefield = datefield.content if datefield else ''
        date = settings.date
        btn = False
        if isinstance(date, datetime):
            btn =  datetime.now().day >= date.day
            if datetime.now() > date:
                settings.date = None
                settings.save()

        if isinstance(settings.date, datetime):
            date = f"{datefield} {settings.date.strftime('%d.%m.%Y %H:%M')}"
            place = block2.item.filter(order=2).first()
        else:
            date = f"Дату и место проведения уточняйте по телефону"
            place = None



        context = {'settings':settings, 'navblock':navblock, 'block1': block1, 'block2': block2, 'block3': block3,
                   'block4': block4, 'block5': block5, 'block6': block6, 'photo1':photo1, 'photo2':photo2,
                   'photo3':photo3, 'photo4':photo4, "date":date, "place":place, 'btn':btn}
        return render(request, 'includes/index.html', context)

class Registry(View):
    def post(self, request):
        if "name" in request.POST and "tel" in request.POST:
            subject = 'Новая заявка на проект "День Милосердия"'
            message = f'Заявка на участие в проекте "День Милосердия".\nФИО: {request.POST["name"]}' \
                      f'\nТелефон: {request.POST["tel"]}'
            settings = models.Settings.objects.get()
            email = settings.email
            filename = os.path.join(sts.BASE_DIR, 'registry_log.txt')
            if settings.date is not None and datetime.now().date() >= settings.date.date():
                return JsonResponse({"error":"1"})
            try:
                send_mail(subject, message, sts.DEFAULT_FROM_EMAIL, (email,))
            except Exception as e:
                print(e)
                try:
                    with open(filename, 'a', encoding='utf-8') as inp:
                        inp.write(str(datetime.now()) + str(request.POST["name"]) + str(request.POST["tel"]) + str(e) + "\n")
                except Exception as err:
                    print(err)
                return JsonResponse({"error":"1"})
            try:
                with open(filename, 'a', encoding='utf-8') as inp:
                    inp.write(
                        str(datetime.now()) + str(request.POST["name"]) + str(request.POST["tel"]) + "\n")
            except Exception as err:
                print(err)
            try:
                if not os.path.isfile(helpers.filename):
                    helpers.write_sheet(table=[], addition=[f'{request.POST["name"]}', f'{request.POST["tel"]}'] )
                else:
                    current_sheet = helpers.extract_sheet()
                    current_table = helpers.xl_to_list(current_sheet)
                    helpers.write_sheet(current_table, [f'{request.POST["name"]}', f'{request.POST["tel"]}'] )
            except Exception as error:
                print(error)
            return JsonResponse({})
        else:
            return JsonResponse({})

