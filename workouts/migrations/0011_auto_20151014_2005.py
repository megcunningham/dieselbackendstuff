# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0010_auto_20151014_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='split',
            name='workouts',
        ),
        migrations.AddField(
            model_name='split',
            name='workouts',
            field=models.ForeignKey(to='workouts.Workout', default=1),
            preserve_default=False,
        ),
    ]
