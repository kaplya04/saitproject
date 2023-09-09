from django import forms
from .models import *


class BackForm(forms.ModelForm):
    class Meta:
        model = Modal
        fields = ('name', 'email','problem','number')
