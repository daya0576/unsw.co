# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_auto_20160202_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
    ]
