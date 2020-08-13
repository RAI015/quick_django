from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('temp', views.temp, name='temp'),
    path('list', views.list, name='list'),
    path('iftag', views.iftag, name='iftag'),
    path('yesno', views.yesno, name='yesno'),
    path('firstof', views.firstof, name='firstof'),
    path('forloop', views.forloop, name='forloop'),
    path('forempty', views.forempty, name='forempty'),
    path('escape', views.escape, name='escape'),
    path('master', views.master, name='master'),
    path('include', views.include, name='include'),
    path('date_time', views.date_time, name='date_time'),
    path('filter', views.filter, name='filter'),
    path('exclude', views.exclude, name='exclude'),
    # path('get', views.get, name='get'),
    path('groupby', views.groupby, name='groupby'),
    path('raw', views.raw, name='raw'),
]
