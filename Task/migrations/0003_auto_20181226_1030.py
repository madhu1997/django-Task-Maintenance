# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-26 05:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_auto_20181226_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessiondetails',
            name='tid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]