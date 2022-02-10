from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from accounts.forms import SignupForm

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.db.models import QuerySet
from django.http import HttpRequest
from django.shortcuts import resolve_url
from django.template.loader import render_to_string


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"

    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)

    name = models.CharField('이름', max_length=100)
    gender = models.CharField('성별', max_length=1, blank=True, choices=GenderChoices.choices)
    profile_img = models.ImageField('프로필이미지', blank=True, upload_to="accounts/profile_img/%Y/%m/%d",
                                    help_text="gif/png/jpg 이미지를 업로드해주세요.")

    class ProviderTypeCodeChoices(models.TextChoices):
        LOCAL = "local", "로컬"
        KAKAO = "kakao", "카카오"

    gender = models.CharField('성별', max_length=1, blank=True, choices=GenderChoices.choices)
    avatar = models.ImageField('아바타', blank=True, upload_to="accounts/avatar/%Y/%m/%d",
                               help_text="100px * 100px 크기의 gif/png/jpg 이미지를 업로드해주세요.")

    provider_type_code = models.CharField("프로바이더 타입코드", max_length=20, choices=ProviderTypeCodeChoices.choices,
                                          default=ProviderTypeCodeChoices.LOCAL)

    provider_accounts_id = models.PositiveIntegerField("프로바이더 회원번호", default=0)

    @staticmethod
    def login_with_kakao(request: HttpRequest, provider_accounts_id):
        provider_type_code = User.ProviderTypeCodeChoices.KAKAO
        qs: QuerySet = User.objects.filter(provider_type_code=provider_type_code,
                                           provider_accounts_id=provider_accounts_id)

        if not qs.exists():
            username = provider_type_code + "__" + str(provider_accounts_id)
            name = provider_type_code + "__" + str(provider_accounts_id)
            email = ""
            password = ""

            user = User.join(username=username, email=email, password=password, first_name=name,
                             provider_type_code=provider_type_code,
                             provider_accounts_id=provider_accounts_id)

        else:
            user: User = qs.first()

        login(request, user)

    @classmethod
    def signup(cls, username, email, password, name, provider_type_code, provider_accounts_id) -> User:

        user = User.objects.create_user(username=username, email=email, password=password, name=name,
                                        provider_type_code=provider_type_code,
                                        provider_accounts_id=provider_accounts_id)

        cls.after_signup(user)

        return user

    @classmethod
    def signup_by_form(cls, form: SignupForm) -> User:
        user = form.save()

        cls.after_signup(user)
        return user

    @staticmethod
    def after_signup(user: User) -> None:
        user.send_welcome_email()


    # https://github.com/askcompany-kr/django-with-react-rev2/ 참조
    def send_welcome_email(self) -> None:

        if not self.email:
            return

        subject = render_to_string("accounts/welcome_email_subject.txt", {
            "user": self,
        })
        content = render_to_string("accounts/welcome_email_content.txt", {
            "user": self,
        })

        sender_email = settings.WELCOME_EMAIL_SENDER

        send_mail(subject, content, sender_email, [self.email], fail_silently=False)


