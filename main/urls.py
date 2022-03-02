from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create_user', views.create_user, name='create_user'),
    path('login', views.login, name='login'),
]