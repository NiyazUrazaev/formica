import os

from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    """Модель профиля пользователя"""

    def path(instance, filename):
        return os.path.join(instance.last_name + instance.first_name,
                            filename)

    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения',
    )

    info = models.TextField(
        default='',
        verbose_name='Информация о пользователе',
        null=True,
        blank=True,
    )

    bio = models.TextField(
        default='',
        verbose_name='Происхождение пользователя',
        null=True,
        blank=True,
    )

    is_prime = models.BooleanField(
        default=False,
        verbose_name='Есть ли подписка',
    )

    country = models.CharField(
        max_length=100,
        verbose_name='Страна',
        blank=True,
        null=True,
    )

    city = models.CharField(
        max_length=100,
        verbose_name='Город',
        blank=True,
        null=True,
    )

    friend = models.ManyToManyField(
        'self',
        verbose_name='Друзья',
        null=True,
        blank=True,
    )

    avatar = models.FileField(
        upload_to=path,
        null=True,
        blank=True,
        verbose_name='Аватар',
    )

    def save(self, *args, **kwargs):
        # Создание нового пользователя
        if self.pk is None:
            # Сохраняем хэш пароля, а не сам пароль
            self.set_password(self.password)
        return super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
