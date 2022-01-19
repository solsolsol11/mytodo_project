from django.urls import path

from su_list import views

app_name = 'su_list'

urlpatterns = [

path('', views.green_list_, name="list"),
path('create1/', views.green_list_create, name="green_list_create")

]