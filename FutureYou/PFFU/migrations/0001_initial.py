# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareerGoal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Status', models.BooleanField(default=True)),
                ('FormInfo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CareerValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Status', models.BooleanField(default=True)),
                ('FileLink', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CareerVoyage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewSkills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Status', models.BooleanField(default=True)),
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
            name='ProgressionBar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CurrentProgress', models.IntegerField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchEmployer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('StaffId', models.CharField(default=b'', max_length=100, serialize=False, primary_key=True)),
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
                ('created', models.DateTimeField(auto_now_add=True)),
                ('studentId', models.CharField(default=b'', max_length=100, serialize=False, primary_key=True)),
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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('StudyYear', models.CharField(max_length=20)),
                ('FirstProgram', models.CharField(max_length=100)),
                ('SecondProgram', models.CharField(max_length=100)),
                ('FirstMajor', models.CharField(max_length=100)),
                ('SecondMajor', models.CharField(max_length=100)),
                ('Work_exp', models.CharField(max_length=30)),
                ('Volunteer_exp', models.CharField(max_length=30)),
                ('Detail_work', models.TextField()),
                ('Detail_volunteer', models.TextField()),
                ('StudentId', models.ForeignKey(to='PFFU.Student')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='StudentId',
            field=models.ForeignKey(to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='researchjob',
            name='StudentId',
            field=models.ForeignKey(to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='researchemployer',
            name='StudentId',
            field=models.ForeignKey(to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='progressionbar',
            name='StudentId',
            field=models.ForeignKey(to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='interviewskills',
            name='StudentId',
            field=models.ForeignKey(to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='careervoyage',
            name='StudentId',
            field=models.ForeignKey(to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='careervalue',
            name='StudentId',
            field=models.ForeignKey(to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='careergoal',
            name='StudentId',
            field=models.ForeignKey(to='PFFU.Student'),
        ),
    ]
