# Generated by Django 3.1.3 on 2020-12-05 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_role',
            field=models.CharField(choices=[('Рекрутер', 'Ищу сотрудников!'), ('Пользователь', 'Ищу работу!')], default='Ищу работу!', max_length=32),
        ),
    ]
