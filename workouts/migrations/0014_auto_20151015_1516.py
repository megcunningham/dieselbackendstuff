# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0013_auto_20151014_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='split',
            name='workouts',
        ),
        migrations.AddField(
            model_name='split',
            name='workouts',
            field=models.ManyToManyField(to='workouts.Workout'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='level',
            field=models.ForeignKey(to='workouts.DifficultyLevel', null=True),
        ),
    ]
