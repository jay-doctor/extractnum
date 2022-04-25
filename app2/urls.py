from django.contrib import admin
from django.urls import path
from .views  import home, delete_matrix
from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', home),
    path('delete/',delete_matrix),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
