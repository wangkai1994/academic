# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 08:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_name', models.CharField(max_length=100, verbose_name='会议名称')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('meeting_address', models.CharField(max_length=100, verbose_name='会议地址')),
                ('meeting_plan', models.CharField(max_length=500, verbose_name='会议安排')),
                ('create_time', models.DateTimeField(verbose_name='创建时间')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
        ),
        migrations.RenameField(
            model_name='thesisinfo',
            old_name='creationTime',
            new_name='create_time',
        ),
    ]
