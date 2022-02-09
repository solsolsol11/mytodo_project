from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm, PasswordResetForm
from django import forms
from django.contrib.auth.hashers import check_password

from .models import User


class FindUsernameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['name'].required = True

    class Meta:
        model = User
        fields = ['name', 'email']


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['name'].required = True
        self.fields['username'].label = '아이디'
        self.fields['profile_img'].widget.attrs['accept'] = 'image/png, image/gif, image/jpeg'

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'name', 'gender', 'profile_img']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
        return email


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['name'].required = True
        self.fields['username'].label = '아이디'
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['profile_img'].widget.attrs['accept'] = 'image/png, image/gif, image/jpeg'
        self.fields['password'].widget = forms.HiddenInput()

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['username', 'name', 'email', 'gender', 'profile_img']

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email).exclude(username=username)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
        return email

class MyPasswordResetForm(PasswordResetForm):
    pass


class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'class': 'form-control',}),)
    def __init__(self,user,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')
