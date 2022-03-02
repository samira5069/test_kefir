from .models import User
from django.forms import ModelForm, TextInput, PasswordInput, DateInput, Textarea


class UserForm(ModelForm):
    class Meta:
        model = User
        fields=["login","password","first_name","last_name","other_name","email","phone","birthday","city","additional_info"]
        widgets={
            "login":TextInput(attrs={
                'placeholder':'Введите login'
            }),
            "password":PasswordInput(attrs={
                'placeholder':'Введите пароль'
            }),
            "first_name":TextInput(attrs={
                'placeholder':'Введите имя'
            }),
             "last_name":TextInput(attrs={
                'placeholder':'Введите фамилию'
            }),
             "other_name":TextInput(attrs={
                'placeholder':'Введите отчество'
            }),
            "email":TextInput(attrs={
                'placeholder':'Введите email'
            }),
            "phone":TextInput(attrs={
                'placeholder':'Введите номер телефона'
            }),
            "birthday":DateInput(attrs={
                'placeholder':'Введите день рождения'
            }),
            "city":TextInput(attrs={
                'placeholder':'Введите город'
            }),
            "additional_info":Textarea(attrs={
                'placeholder':'Введите дополнительную информацию'
            }),
        }

