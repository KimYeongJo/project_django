from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import *

# Create your views here.
class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:post-list')
        form = RegisterForm()
        context = {
            'title': '회원가입',
            'form': form
        }
        return render(request, 'user/register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user:login')


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:post-list')
        form = LoginForm()
        context = {
            'title': '로그인',
            'form': form
        }
        return render(request, 'user/login.html', context)
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:post-list')
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)

            if user:
                login(request, user)
                return redirect('index')
        context = {
            'title': '로그인',
            'form': form
        }
        return render(request, 'user/login.html', context)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')