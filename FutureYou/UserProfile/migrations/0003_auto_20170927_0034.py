# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-27 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0002_auto_20170927_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicprofile',
            name='study_status',
            field=models.CharField(blank=True, choices=[('U', 'Undergraduate'), ('P', 'Postgraduate')], default='U', max_length=32, verbose_name='Study Status'),
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='profile_id',
            field=models.CharField(default='e99aee74361445be867b8ba728803e64', editable=False, max_length=64, primary_key=True, serialize=False),
        ),
    ]
