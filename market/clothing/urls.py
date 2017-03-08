from django.conf.urls import url
from clothing import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),


]