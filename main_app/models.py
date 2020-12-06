from django.db import models
from django.urls import reverse


class CVModel(models.Model):
    position = models.CharField(max_length=128, blank=False)

    def get_absolute_url(self):
        return reverse('cv_update', args=(self.id,))
