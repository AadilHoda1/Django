# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-18 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0037_auto_20171118_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='Progress',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='Team_Members',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
    ]