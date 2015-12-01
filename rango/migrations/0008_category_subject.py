# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subject',
            field=models.ForeignKey(default=1, to='rango.Subject'),
            preserve_default=False,
        ),
    ]
