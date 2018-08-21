from django.urls import path

from . import views

urlpatterns = [
    path('', views.fuck_view_func, name='index'),
]
