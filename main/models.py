from tabnanny import verbose
from django.db import models


class Task(models.Model):
    title=models.CharField('Название', max_length=50)
    task=models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Задача'
        verbose_name_plural='Задачи'

class User(models.Model):
    login=models.CharField('login', max_length=50)
    password=models.CharField('pass', max_length=50)
    first_name=models.CharField('Имя', max_length=50)
    last_name=models.CharField('Фамилия', max_length=50)
    other_name=models.CharField('Отчество', max_length=50)
    email=models.CharField('Почта', max_length=50)
    phone=models.CharField('Телефон', max_length=50)
    birthday=models.DateField('День рождения')
    city=models.CharField('Город',max_length=50)
    additional_info=models.CharField('Дополнительная информация',max_length=50)
    is_admin=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name