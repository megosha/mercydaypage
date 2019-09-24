from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
from indexpage import models
from django.core.mail import send_mail




# Create your views here.

class Home(View):
    def dispatch(self, request, *args, **kwargs):
        return HttpResponseRedirect('index')


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

        context = {'settings':settings, 'navblock':navblock, 'block1': block1, 'block2': block2, 'block3': block3,
                   'block4': block4, 'block5': block5, 'block6': block6,
                   'photo1':photo1, 'photo2':photo2, 'photo3':photo3, 'photo4':photo4}
        return render(request, 'includes/index.html', context)

class Registry(View):
    def post(self, request):
        if "name" in request.POST and "tel" in request.POST:
            # print("HERE")
            subject = 'Новая заявка на проект "День Милосерия"'
            message = f'Заявка на участие в проекте "День Милосердия".\nФИО: {request.POST["name"]}' \
                      f'\nТелефон: {request.POST["tel"]}'
            from_email = 'utils@electis.ru'
            settings = models.Settings.objects.get()
            email = settings.email
            try:
                send_mail(subject, message, from_email, (email,))#, fail_silently=True)
            except Exception as e:
                print(e)
                return JsonResponse({"error":"1"})
            return JsonResponse({})
        else:
            return JsonResponse({})
