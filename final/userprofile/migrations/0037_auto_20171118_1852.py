# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-18 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0036_auto_20171118_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='Progress',
            field=models.IntegerField(null=True),
        ),
    ]
