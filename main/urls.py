from django.urls import path
from django.views.decorators.cache import cache_page

from config.settings import CACHE_ENABLED
from main.views import index

urlpatterns = []

if CACHE_ENABLED:
    urlpatterns.append(path('', cache_page(60)(index), name='index'))
else:
    urlpatterns.append(path('', index, name='index'))
