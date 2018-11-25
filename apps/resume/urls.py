from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^experience$', views.experience),
    url(r'^education$', views.education),
    url(r'^contact$', views.contact),
]