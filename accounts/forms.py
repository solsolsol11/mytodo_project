from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

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
        self.fields['profile_img'].widget.attrs['accept'] = 'image/png, image/gif, image/jpeg'
        self.fields['password'].widget = forms.HiddenInput()
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['name', 'email', 'gender', 'profile_img']

