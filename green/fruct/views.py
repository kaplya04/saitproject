from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, ListView
# Create your views here.
from reportlab.lib.randomtext import objects
from . import models
from .models import *


def fruct(request):
    ind = tovar.objects.all()
    data = {
        'ind': ind,
    }
    return render(request, "fruct/index.html", context=data)


def index(request):
    num_img = Images.objects.all().count()

    return render(request, 'index.html', context={'num_img': num_img})


def myview(request):
    data = {"header": "Text"}
    return render(request, "base.html", context=data)


def m(request):
    a = postgrey.objects.all()
    data = {
        'a': a,
    }
    return render(request, "fruct/person.html", data)


class SearchResultsView(ListView):
    model = tovar
    template_name = 'fruct/search.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = tovar.objects.filter(
            Q(name__icontains=query)
        )
        return object_list


class mypoiskfruct(DetailView):
    model = tovar
    template_name = 'fruct/description.html'
    context_data = 'din'
#Практика

