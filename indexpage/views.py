from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
from indexpage import models
# from django.views.decorators.csrf import csrf_exempt





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
        context = {'navblock':navblock, 'block1': block1, 'block2': block2, 'block3': block3,
                   'block4': block4, 'block5': block5, 'block6': block6,
                   'photo1':photo1, 'photo2':photo2, 'photo3':photo3, 'photo4':photo4}
        return render(request, 'includes/index.html', context)

class Registry(View):
    # @csrf_exempt
    def post(self, request):
        if "name" in request.POST and "tel" in request.POST:
            print("HERE")
            return JsonResponse({})
        else:
            return JsonResponse({})
