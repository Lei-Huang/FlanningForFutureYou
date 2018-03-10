# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BadgeId', models.CharField(max_length=20)),
                ('BadgeStatus', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BadgeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BageInfoId', models.CharField(max_length=20)),
                ('BageName', models.CharField(max_length=40)),
                ('Deprecation', models.TextField()),
                ('Relatiom', models.CharField(max_length=50)),
                ('Imageurl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Incentive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('IncentiveId', models.CharField(max_length=20)),
                ('IncentiveType', models.CharField(max_length=30)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('StudentId', models.CharField(default=b'', max_length=100, blank=True)),
                ('StaffId', models.CharField(default=b'', max_length=100, blank=True)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='MainEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('EventId', models.CharField(max_length=20)),
                ('EvenType', models.CharField(max_length=20)),
                ('EventDate', models.DateTimeField()),
                ('EventContent', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PointsId', models.CharField(max_length=20)),
                ('CurrentPoints', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('StaffId', models.CharField(default=b'', max_length=100, blank=True)),
                ('FirstName', models.CharField(max_length=60)),
                ('LastName', models.CharField(max_length=60)),
                ('Email', models.EmailField(max_length=254, verbose_name=b'e-mail', blank=True)),
                ('PhoneNumber', models.CharField(max_length=30)),
                ('ModifyDate', models.DateTimeField()),
                ('Description', models.TextField()),
                ('UserProfileYear', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('studentId', models.CharField(default=b'', max_length=100, blank=True)),
                ('FirstName', models.CharField(max_length=60)),
                ('LastName', models.CharField(max_length=60)),
                ('Degree', models.CharField(max_length=30)),
                ('Discipline', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('residentStatus', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=60)),
                ('graduation_year', models.CharField(max_length=30)),
                ('YearOfStudy', models.CharField(max_length=10)),
                ('highlighted', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UserEventId', models.CharField(max_length=20)),
                ('UserEventType', models.CharField(max_length=20)),
                ('UserEventDate', models.DateTimeField()),
                ('UserEventContent', models.TextField()),
                ('StudentId', models.ForeignKey(to='PFFU.Student')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ProfileYear', models.CharField(max_length=20)),
                ('ProfileType', models.CharField(max_length=20)),
                ('NetworkTree', models.CharField(max_length=30)),
                ('SkillTree', models.CharField(max_length=30)),
                ('ExperienceTree', models.CharField(max_length=30)),
                ('PreparationTree', models.CharField(max_length=30)),
                ('Work_exp', models.CharField(max_length=30)),
                ('Volunteer_exp', models.CharField(max_length=30)),
                ('Detail_work', models.TextField()),
                ('Detail_volunteer', models.TextField()),
                ('Network', models.TextField()),
                ('Skill', models.TextField()),
                ('Experience', models.TextField()),
                ('Preparation', models.TextField()),
                ('Notes', models.TextField()),
                ('StudentId', models.ForeignKey(to='PFFU.Student')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='StudentId',
            field=models.ForeignKey(to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='badge',
            name='BadgeInfo',
            field=models.ForeignKey(to='PFFU.BadgeInfo'),
        ),
    ]
