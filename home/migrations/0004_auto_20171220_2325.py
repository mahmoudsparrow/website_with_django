# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-20 21:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_friend_to_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='to_user',
        ),
        migrations.AddField(
            model_name='friend',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]