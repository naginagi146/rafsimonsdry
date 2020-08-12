from django.urls import path
from . import views
from django.conf.urls import url  
from django.conf import settings #追加   
from django.conf.urls.static import static #追加

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #追加