# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_remove_answers_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='edit_date',
            field=models.DateTimeField(default='2015-11-28 11:21:13.288000'),
            preserve_default=False,
        ),
    ]
