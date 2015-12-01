# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0012_auto_20151201_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='course_name',
            new_name='name',
        ),
    ]
