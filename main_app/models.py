from django.db import models
from django.urls import reverse
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import get_current_authenticated_user


class CVModel(models.Model):
    created_by = CurrentUserField(default=get_current_authenticated_user, blank=False)
    position = models.CharField(max_length=128, blank=False)

    def get_absolute_url(self):
        return reverse('cv_update', args=(self.id,))
