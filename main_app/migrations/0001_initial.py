# Generated by Django 3.1.3 on 2020-12-06 22:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CVModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('position', models.CharField(max_length=128)),
                ('salary', models.PositiveIntegerField()),
                ('personal_info', models.TextField()),
                ('skills', models.TextField()),
                ('selected_language', models.CharField(choices=[('french', 'Французский'), ('english', 'Английский'), ('german', 'Немецкий')], default='english', max_length=32)),
                ('created_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
