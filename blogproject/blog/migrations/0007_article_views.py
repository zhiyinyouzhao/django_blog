# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-15 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170509_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
