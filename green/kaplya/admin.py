from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Kategoria)
admin.site.register(Modal)
admin.site.register(News)