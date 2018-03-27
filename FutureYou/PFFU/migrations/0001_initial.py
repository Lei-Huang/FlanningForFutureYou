# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-26 23:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareerGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.BooleanField(default=True)),
                ('Sector', models.CharField(max_length=30)),
                ('FirstRow', models.CharField(max_length=100)),
                ('SecondRow', models.CharField(max_length=100)),
                ('ThirdRow', models.CharField(max_length=100)),
                ('FirstPlan', models.TextField()),
                ('SecondPlan', models.TextField()),
                ('ThirdPlan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CareerValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.BooleanField(default=True)),
                ('FormInfo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CareerVoyage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentId', models.CharField(blank=True, default='', max_length=100)),
                ('StaffId', models.CharField(blank=True, default='', max_length=100)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ProgressionBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CurrentProgress', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchEmployer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('StaffId', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=60)),
                ('LastName', models.CharField(max_length=60)),
                ('Email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
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
                ('studentId', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudyYear', models.CharField(max_length=20)),
                ('FirstProgram', models.CharField(max_length=100)),
                ('SecondProgram', models.CharField(max_length=100)),
                ('FirstMajor', models.CharField(max_length=100)),
                ('SecondMajor', models.CharField(max_length=100)),
                ('WorkStartDate', models.CharField(max_length=50)),
                ('Work_exp', models.CharField(max_length=30)),
                ('WorkEndDate', models.CharField(max_length=50)),
                ('Volunteer_exp', models.CharField(max_length=30)),
                ('Detail_work', models.TextField()),
                ('Detail_volunteer', models.TextField()),
                ('StudentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PFFU.Student')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='StudentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='researchjob',
            name='StudentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='researchemployer',
            name='StudentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='progressionbar',
            name='StudentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='interviewskills',
            name='StudentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='careervoyage',
            name='StudentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='careervalue',
            name='StudentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PFFU.Student'),
        ),
        migrations.AddField(
            model_name='careergoal',
            name='StudentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PFFU.Student'),
        ),
    ]
