# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20151128_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='post_date',
            field=models.DateTimeField(),
        ),
    ]
