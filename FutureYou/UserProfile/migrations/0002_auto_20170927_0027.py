# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-27 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicprofile',
            name='id',
        ),
        migrations.AddField(
            model_name='basicprofile',
            name='profile_id',
            field=models.CharField(default='192512f3ce984299a3774ea901942019', max_length=64, primary_key=True, serialize=False),
        ),
    ]
