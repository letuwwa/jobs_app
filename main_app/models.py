from datetime import datetime

from django.db import models
from django.urls import reverse
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import get_current_authenticated_user


class CVModel(models.Model):
    created_by = CurrentUserField(default=get_current_authenticated_user, blank=False)
    date = models.DateTimeField(default=datetime.now, blank=False)
    position = models.CharField(max_length=128, blank=False)
    salary = models.PositiveIntegerField(blank=False, null=False)
    personal_info = models.TextField()
    skills = models.TextField()

    french = 'french'
    english = 'english'
    german = 'german'

    LANGUAGE = [
        (french, 'Французский'),
        (english, 'Английский'),
        (german, 'Немецкий'),
    ]
    selected_language = models.CharField(
        max_length=32,
        choices=LANGUAGE,
        default=english,
    )

    def get_absolute_url(self):
        return reverse('cv_update', args=(self.id,))
