# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20151128_1812'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Editor',
            new_name='BaiduEditor',
        ),
    ]
