# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20151129_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=100, blank=True)),
                ('school_cn', models.CharField(max_length=100, blank=True)),
                ('school_en', models.CharField(max_length=100, blank=True)),
            ],
        ),
    ]
