from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    re_path(r'^lista/$', views.TeacherList.as_view()),
    re_path(r'^detalle/(?P<id>\d+)$', views.TeacherDetail.as_view()),
]