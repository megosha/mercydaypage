from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
from indexpage import models
from django.core.mail import send_mail
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
        if isinstance(date, datetime) and datetime.now() > date:
            settings.date = None
            settings.save()

        if isinstance(settings.date, datetime):
            date = f"{datefield} {settings.date.strftime('%d.%m.%Y %H:%M')}"
            place = block2.item.filter(order=2).first()
        else:
            date = f"Дату и место проведения уточняйте по телефону"
            place = None



        context = {'settings':settings, 'navblock':navblock, 'block1': block1, 'block2': block2, 'block3': block3,
                   'block4': block4, 'block5': block5, 'block6': block6,
                   'photo1':photo1, 'photo2':photo2, 'photo3':photo3, 'photo4':photo4, "date":date, "place":place}
        return render(request, 'includes/index.html', context)

class Registry(View):
    def post(self, request):
        if "name" in request.POST and "tel" in request.POST:
            # print("HERE")
            subject = 'Новая заявка на проект "День Милосердия"'
            message = f'Заявка на участие в проекте "День Милосердия".\nФИО: {request.POST["name"]}' \
                      f'\nТелефон: {request.POST["tel"]}'
            from_email = 'utils@electis.ru'
            settings = models.Settings.objects.get()
            email = settings.email
            filename = os.path.join('/www', 'mercydaypage', 'registry_log.txt')
            try:
                send_mail(subject, message, from_email, (email,))#, fail_silently=True)
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
            return JsonResponse({})
        else:
            return JsonResponse({})
