from django.urls import path

from su_list import views

app_name = 'su_list'

urlpatterns = [

path('', views.list, name="list"),
path('create/', views.list_create, name="list__create")

]