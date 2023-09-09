from django.forms import forms

from .models import *


class klient(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = klient
        fields = ('id', 'name', 'price', 'cover')


class MyForm(forms.Form):
    class Meta:
        model = tovar
        fields = ('id', 'name', 'price', 'cover')
