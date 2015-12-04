# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mealnumber',
            name='diet',
        ),
        migrations.AddField(
            model_name='meal',
            name='diet',
            field=models.ForeignKey(default=2, to='diets.Diet'),
            preserve_default=False,
        ),
    ]
