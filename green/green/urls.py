
from django.urls import path, re_path
from django.contrib import admin
from django.urls import *
from fruct.views import *
from green import settings
from django.conf.urls.static import static
from kaplya.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', fruct, name='fruct'),
    path('search/', SearchResultsView.as_view(), name='results'),
    path('index/<int:pk>', mypoiskfruct.as_view(), name='mypoiskfruct'),
    path('praktika/', index, name='prak'),
    path('post/<int:id>/', kategoria, name='post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
