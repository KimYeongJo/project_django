from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': '아이디',
            'password': '비밀번호'
        }


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': '아이디',
            'password': '비밀번호'
        }