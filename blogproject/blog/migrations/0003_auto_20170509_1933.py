# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170507_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='modified_time',
            field=models.DateField(),
        ),
    ]
