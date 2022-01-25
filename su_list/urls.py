from django.urls import path

from su_list import views

app_name = 'su_list'

urlpatterns = [

    path('', views.all_list, name="list"),
    path('test/', views.test_case, name="test"),
    path('create1/', views.green_list_create, name="green_list_create"),
    path('create2/', views.red_list_create, name="red_list_create"),
    path('create3/', views.gray_list_create, name="gray_list_create"),
    path('create4/', views.gold_list_create, name="gold_list_create"),
    path('delete1_list/', views.green_list_delete, name='green_list_delete'),
    path('delete1_all_list/', views.green_list_all_delete, name='green_all_delete'),
    path('delete2_list/', views.red_list_delete, name='red_list_delete'),
    path('delete3_list/', views.gray_list_delete, name='gray_list_delete'),
    path('delete4_list/', views.gold_list_delete, name='gold_list_delete'),

]
