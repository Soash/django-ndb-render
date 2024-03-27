from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

handler404 = views.custom_404_page
