# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0011_subject_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
