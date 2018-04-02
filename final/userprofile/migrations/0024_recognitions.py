# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-10 18:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0023_auto_20171110_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recognitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('Description', models.TextField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Recognitions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]