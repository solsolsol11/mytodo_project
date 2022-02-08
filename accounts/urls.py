from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts import views
from accounts.forms import MyPasswordResetForm

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
    path('reset_password/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('accounts:password_reset_complete'),
        template_name='accounts/password_reset_form.html',
        email_template_name='accounts/password_reset_email.html',
        form_class=MyPasswordResetForm
    ), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounts:password_reset_complete')
    ), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'accounts/password_reset_sent.html'
    ), name='password_reset_complete'),
]
