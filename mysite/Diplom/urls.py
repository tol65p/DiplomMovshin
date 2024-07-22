from django.urls import path
from . import views
app_name = 'Diplom'
urlpatterns = [path('', views.index, name='index'),
               path('reg', views.reg, name='reg'),
               path('entry', views.entry, name='entry'),
               path('runner', views.runner, name='runner'),
               path('event', views.event, name='event'),
               path('RegEvent', views.RegEvent, name='RegEvent'),
               path('EnterResults', views.EnterResults, name='EnterResults'),
               path('WiewResults', views.WiewResults, name='WiewResults'),
               path('exit', views.exit, name='exit')
              ]