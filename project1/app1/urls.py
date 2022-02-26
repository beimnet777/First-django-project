from django.urls import path

from . import views

urlpatterns=[path('',views.home,name="home"),
path('add/num',views.add),
path('numform',views.createNum,name='numsform')]