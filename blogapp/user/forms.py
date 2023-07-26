from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms.widgets import PasswordInput, TextInput

User = get_user_model()


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username']

    username = forms.CharField(
        widget=TextInput(
            attrs={'placeholder': '아이디'}))
    password1 = forms.CharField(
        widget=PasswordInput(
            attrs={'placeholder':'비밀번호'}))
    password2 = forms.CharField(
        widget=PasswordInput(
            attrs={'placeholder':'비밀번호 확인'}))


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
    
    username = forms.CharField(
        widget=TextInput(
            attrs={'placeholder': '아이디'}))
    password = forms.CharField(
        widget=PasswordInput(
            attrs={'placeholder':'비밀번호'}))