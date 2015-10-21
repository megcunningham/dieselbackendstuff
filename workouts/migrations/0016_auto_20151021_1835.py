# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0015_auto_20151015_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseset',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
