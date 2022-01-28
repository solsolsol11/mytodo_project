from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
    path('find_username/', views.find_username, name='find_username'),
    path('signin/kakao/', views.kakao_login, name='kakao_signin'),
    path('signin/kakao/callback/', views.kakao_signin_callback, name='kakao_signin_callback'),
    path('change_password/', views.change_password, name='change_password'),
    path('update/', views.update, name='update'),
    path('profile/', views.profile, name='profile'),
    path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
