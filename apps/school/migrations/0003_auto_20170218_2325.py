# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20170217_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='course_id', serialize=False, to='school.Course')),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
    ]