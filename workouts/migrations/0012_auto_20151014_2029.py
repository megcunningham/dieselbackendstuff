# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0011_auto_20151014_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weeklyworkout',
            name='split',
        ),
        migrations.AddField(
            model_name='split',
            name='week_of',
            field=models.ForeignKey(default=1, to='workouts.WeeklyWorkout'),
            preserve_default=False,
        ),
    ]
