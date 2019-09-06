from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from indexpage import models


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
        context = {'navblock':navblock, 'block1': block1, 'block2': block2, 'block3': block3,
                   'block4': block4, 'block5': block5, 'block6': block6}
        return render(request, 'includes/index.html', context)
