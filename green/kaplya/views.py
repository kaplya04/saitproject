# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, ListView
# Create your views here.
from reportlab.lib.randomtext import objects
from . import models
from .forms import BackForm
from .models import *


def index(request):
    categoriya = Kategoria.objects.all()
    new = News.objects.all()
    if request.method == 'POST':
        form = BackForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BackForm()
    data = {
        'categoriya': categoriya,
        'new': new,
        'form': form,
    }
    return render(request, "kaplya/praktika.html", data)


def kategoria(request, id):
    newss = News.objects.filter(kategoria_id=id)
    categor = Kategoria.objects.all()
    data = {
        'newss': newss,
        'categor': categor,
    }
    return render(request, "kaplya/praktika.html", data)