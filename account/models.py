from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)

    RECRUITER = 'Рекрутер'
    COMMON_USER = 'Пользователь'

    STATUS = [
        (RECRUITER, 'Ищу сотрудников!'),
        (COMMON_USER, 'Ищу работу!'),
    ]

    user_role = models.CharField(
        max_length=32,
        choices=STATUS,
        default='Ищу работу!',
    )

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
