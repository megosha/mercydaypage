from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
from indexpage import models, helpers, forms
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
        form = forms.Registartion()
        settings = models.Settings.objects.filter().first()
        photos = models.Gallery.objects.all().order_by('order')
        faqs = models.Faq.objects.all().order_by('order')
        faqs_count = faqs.count()
        faqs_1 = faqs[:faqs_count/2]
        faqs_2 = faqs[faqs_count/2:]
        date = settings.date
        date_string = ''
        btn = False
        if date is not None:
            date_string = date.strftime('%Y/%m/%d %H:%M:%S')
            btn = datetime.now() <= date
            if datetime.now() > date:
                settings.date = None
                settings.save()

        context = {'settings':settings, 'photos':photos, 'faqs_1':faqs_1, 'faqs_2':faqs_2,
                   'date_string':date_string,'btn':btn, 'form':form}
        return render(request, 'includes/index.html', context)

class Registry(View):
    def get(self, request):
        return HttpResponseRedirect('/')

    def registry_render(self, request, result=None):
        settings = models.Settings.objects.get()
        context = {"result":result, "settings":settings}
        return render(request, 'includes/registration.html', context)

    def post(self, request):
        form = forms.Registartion(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            subject = 'Новая заявка на проект "День Милосердия"'
            message = f'Заявка на участие в проекте "День Милосердия".\nФИО: {name}' \
                      f'\nТелефон: {phone}'
            settings = models.Settings.objects.get()
            email = settings.email
            filename = os.path.join(sts.BASE_DIR, 'registry_log.txt')
            if settings.date is not None and datetime.now().date() >= settings.date.date():
                return self.registry_render(request, result=False)
            try:
                send_mail(subject, message, sts.DEFAULT_FROM_EMAIL, (email,))
            except Exception as e:
                print(e)
                try:
                    with open(filename, 'a', encoding='utf-8') as inp:
                        inp.write(str(datetime.now()) + name + phone + str(e) + "\n")
                except Exception as err:
                    print(err)
                return self.registry_render(request, result=False)
            try:
                with open(filename, 'a', encoding='utf-8') as inp:
                    inp.write(
                        str(datetime.now()) + name + phone + "\n")
            except Exception as err:
                print(err)
            try:
                valid_date = settings.date.date() if settings.date is not None else 'None'
                fname = helpers.generate_filename(valid_date)
                if not os.path.isfile(fname):
                    helpers.write_sheet(table=[],
                                        addition=[f'{name}', f'{phone}'],
                                        fname=fname)
                else:
                    current_sheet = helpers.extract_sheet(fname=fname)
                    current_table = helpers.xl_to_list(current_sheet)
                    helpers.write_sheet(current_table, [f'{name}', f'{phone}'], fname )
            except Exception as error:
                print(error)
            return self.registry_render(request, result=True)
        else:
            return self.registry_render(request, result=False)

