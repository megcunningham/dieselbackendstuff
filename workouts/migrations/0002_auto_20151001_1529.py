# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='group_name',
            field=models.ForeignKey(default=1, to='workouts.MuscleGroup'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exerciseset',
            name='reps',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='exerciseset',
            name='weight',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
