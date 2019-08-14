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
        return render(request, 'includes/index.html', context={})
