from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    """Модель профиля пользователя"""

    birthday = models.DateField(
        null=True,
        verbose_name='Дата рождения',
    )

    info = models.TextField(
        default='',
        verbose_name='Информация о пользователе',
    )

    bio = models.TextField(
        default='',
        verbose_name='Происхождение пользователя',
    )

    is_prime = models.BooleanField(
        default=False,
        verbose_name='Есть ли подписка',
    )

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
