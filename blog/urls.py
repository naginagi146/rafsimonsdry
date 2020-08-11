from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
urlpatterns = [
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]