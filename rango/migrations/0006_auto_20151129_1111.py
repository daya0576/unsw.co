# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_categoryuserlikes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='author',
            new_name='user',
        ),
    ]
