from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('form_page/',views.form_name_view,name='form_name')

]
