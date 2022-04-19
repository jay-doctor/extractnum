from django.urls import path
from .views  import home, delete_matrix
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('', home),
    path('delete/',delete_matrix)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
