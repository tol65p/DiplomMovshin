from django.urls import path
from . import views
app_name = 'Diplom'
urlpatterns = [path('', views.index, name='index'),
               path('reg', views.reg, name='reg')
              ]