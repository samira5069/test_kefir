# Generated by Django 4.0.2 on 2022-02-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='additional_info',
            field=models.CharField(default=23, max_length=50, verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=0, max_length=50, verbose_name='Город'),
            preserve_default=False,
        ),
    ]
