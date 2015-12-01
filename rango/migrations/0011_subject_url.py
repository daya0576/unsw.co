# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0010_subject_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='url',
            field=models.URLField(default=2),
            preserve_default=False,
        ),
    ]
