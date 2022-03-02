from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import UserForm
from django.contrib.auth import authenticate, login


def index(request):
    tasks=Task.objects.all()
    return render(request, 'main/index.html', {'title':'Главная страница сайта', 'tasks': tasks})

def create_user(request):
    error = ''
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Форма была неверной'

    form=UserForm()
    context={ 
        'form':form,
        'error':error
        }
    return render(request, 'main/create_user.html',context)

def login(request):
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['login'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Авторизация прошла успешно')
                else:
                    return HttpResponse('Пользователя не существует')
            else:
                return HttpResponse('Неверный логин или пароль')
    else:
        form = UserForm()
    return render(request, 'main/login.html', {'form':form})
