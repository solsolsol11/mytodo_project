import os

import requests
from django.contrib import messages
from django.contrib.auth import login as auth_login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth.views import logout_then_login, LoginView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


from django.db.models import QuerySet

from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from lazy_string import LazyString

from .decorators import logout_required
# Create your views here.
from .forms import SignupForm, FindUsernameForm, CustomUserChangeForm
from .models import User


class MyLoginView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/signin.html'
    next_page = "/"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.success_message = LazyString(
            lambda: f'{self.request.user.last_name}{self.request.user.name} 님 환영합니다.')

    def get_initial(self):
        initial = self.initial.copy()
        initial['username'] = self.request.GET.get('username', None)

        return initial


@logout_required
def signin(request: HttpRequest):
    return MyLoginView.as_view()(request)


def signout(request: HttpRequest):
    messages.success(request, "로그아웃 되었습니다.")
    return logout_then_login(request)


@logout_required
def signup(request: HttpRequest):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            signed_user = User.signup_by_form(form)
            auth_login(request, signed_user)
            messages.success(request, "회원가입 환영합니다.")
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


def find_username(request: HttpRequest):
    if request.method == 'POST':
        form = FindUsernameForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['name']
            print(first_name)
            qs: QuerySet = User.objects.filter(email=email, name=first_name)

            if not qs.exists():
                messages.warning(request, "일치하는 회원이 존재하지 않습니다.")
            else:
                user: User = qs.first()
                messages.success(request, f'해당회원의 아이디는 {user.username} 입니다.')
                return redirect(reverse("accounts:signin") + '?username=' + user.username)
    else:
        form = FindUsernameForm()

    return render(request, 'accounts/find_username.html', {
        'form': form,
    })


def kakao_login(request: HttpRequest):
    os.environ.get("KAKAO_APP__REST_API_KEY")
    os.environ.get("KAKAO_APP__LOGIN__REDIRECT_URI")

    REST_API_KEY = os.environ.get("KAKAO_APP__REST_API_KEY")
    REDIRECT_URI = os.environ.get("KAKAO_APP__LOGIN__REDIRECT_URI")

    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code"
    )


class KakaoException(Exception):
    def __init__(self):
        super().__init__('에러메시지')


def kakao_signin_callback(request):
    code = request.GET.get("code")

    REST_API_KEY = os.environ.get("KAKAO_APP__REST_API_KEY")
    REDIRECT_URI = os.environ.get("KAKAO_APP__LOGIN__REDIRECT_URI")

    # (2)
    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&code={code}"
    )
    # (3)

    token_json = token_request.json()

    error = token_json.get("error", None)
    if error is not None:
        raise Exception("카카오 로그인 에러")

    access_token = token_json.get("access_token")

    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    profile_json = profile_request.json()

    id = profile_json.get("id")

    User.login_with_kakao(request, id)

    messages.success(request, "카카오톡 계정으로 로그인되었습니다")

    return redirect("main")


# 비밀번호 변경

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다')
            return redirect('main')
        else:
            messages.error(request, '형식이 잘못되었습니다')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


# 회원정보 수정

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '회원정보가 수정되었습니다')
            return redirect('main')


    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/update.html', {
        'form': form,
    })


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'  # 템플릿을 변경하려면 이와같은 형식으로 입력

    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            opts = {
                'use_https': self.request.is_secure(),
                'token_generator': self.token_generator,
                'from_email': self.from_email,
                'email_template_name': self.email_template_name,
                'subject_template_name': self.subject_template_name,
                'request': self.request,
                'html_email_template_name': self.html_email_template_name,
                'extra_email_context': self.extra_email_context,
            }
            form.save(**opts)
            return super().form_valid(form)
        else:
            return render(self.request, 'accounts/password_reset_done_fail.html')


@require_POST
def delete(request):
    if request.user.is_authenticated:
    	request.user.delete()
        auth_logout(request) # session 지우기. 단 탈퇴후 로그아웃순으로 처리. 먼저 로그아웃하면 해당 request 객체 정보가 없어져서 삭제가 안됨.
    return redirect('articles:index')