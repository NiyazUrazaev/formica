# Generated by Django 3.0.3 on 2020-05-05 21:34

import achievement.models
from django.db import migrations
from django.db import models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aim', '0002_auto_20200506_0017'),
        ('profile_page', '0002_auto_20200429_0534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50,
                                           verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True,
                                                 verbose_name='Описание')),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now,
                    verbose_name='Дата'
                )),
                ('picture', models.FileField(
                    blank=True,
                    null=True,
                    upload_to=achievement.models.Achievement.path,
                    verbose_name='Картинка'
                )),
            ],
            options={
                'verbose_name': 'Достижение',
                'verbose_name_plural': 'Достижения',
            },
        ),
        migrations.CreateModel(
            name='UserAchievement',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now,
                    verbose_name='Дата'
                )),
                ('achievement', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    to='achievement.Achievement',
                    verbose_name='Достижение'
                )),
                ('profile', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='profile_page.Profile',
                    verbose_name='Пользователь'
                )),
                ('user_aim', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='aim.UserAim',
                    verbose_name='Цель пользователя'
                )),
            ],
            options={
                'verbose_name': 'Достижение пользователя',
                'verbose_name_plural': 'Достижения пользователей',
            },
        ),
    ]
