from django.contrib import admin
from django.urls import path
from system import views
from django.conf.urls import url

urlpatterns = [
    url(r'^get_role_name/$', views.GetRoleName.as_view()),
]
