from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    re_path(r'^lista/$', views.StudentList.as_view()),
    re_path(r'^detalle/(?P<id>\d+)$', views.StudentDetail.as_view()),
]