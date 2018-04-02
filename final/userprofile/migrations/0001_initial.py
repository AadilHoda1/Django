# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-03 15:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(max_length=200)),
                ('Departmental_post', models.CharField(max_length=200)),
                ('Room_no', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('Research_interest', models.TextField()),
                ('primary_Research_group', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
