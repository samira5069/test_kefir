# Generated by Django 4.0.2 on 2022-02-24 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_alter_task_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
