import os

from django.db import models
from django.utils.timezone import now

from aim.helpers import get_next_period
from aim.helpers import REGULARITY
from formica.settings import AIM_DIR_NAME


class Aim(models.Model):

    def path(instance, filename):
        return os.path.join(AIM_DIR_NAME, instance.title,
                            filename)

    title = models.CharField(
        max_length=100,
        verbose_name='Название',
    )

    info = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True,
    )

    picture = models.FileField(
        verbose_name='Картинка',
        upload_to=path,
        blank=True,
        null=True,
    )

    rate = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        default=0,
    )

    author = models.ForeignKey(
        'profile_page.Profile',
        verbose_name='Автор цели',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цель'


class UserAim(models.Model):

    profile = models.ForeignKey(
        'profile_page.Profile',
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )

    aim = models.ForeignKey(
        Aim,
        verbose_name='Цель',
        on_delete=models.PROTECT,
    )

    created = models.DateTimeField(
        default=now,
        verbose_name='Дата создания'
    )

    completed = models.DateTimeField(
        verbose_name='Дата выполнения',
        null=True,
        blank=True,
    )

    deadline = models.DateTimeField(
        verbose_name='Крайний срок',
        null=True,
        blank=True,
    )

    is_closed = models.BooleanField(
        default=False,
        verbose_name='Закрыта',
    )

    regularity = models.PositiveSmallIntegerField(
        verbose_name='Регулярность',
        null=True,
        blank=True,
        choices=REGULARITY,
    )

    def save(self, **kwargs):
        self.completed = now()
        if self.regularity and not self.is_closed:
            new_obj = UserAim(
                profile_id=self.profile_id,
                aim_id=self.aim_id,
                deadline=get_next_period(self.completed,
                                         self.regularity),
                regularity=self.regularity,
            )
            new_obj.save()
        return super(UserAim, self).save(**kwargs)




