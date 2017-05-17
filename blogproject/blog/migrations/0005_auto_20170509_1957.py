# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170509_1948'),
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
