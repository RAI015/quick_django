from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('temp', views.temp, name='temp'),
    path('temp_view', views.MyTemplateView.as_view(), name="temp_view"),
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
    path('rel', views.rel, name='rel'),
    path('rel2', views.rel2, name='rel2'),

    path('route_param', views.route_param, name='route_param'),
    # path('route_param/<int:id>', views.route_param, name='route_param'),
    re_path('route_param/(?P<id>[0-9]{2,3})$', views.route_param, name='route_param'),
    # path('search/<path:keywd>', views.search, name='search')
    path('setcookie', views.setcookie, name='setcookie'),
    path('getcookie', views.getcookie, name='getcookie'),
]
