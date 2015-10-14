# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0008_workout_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyWorkout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('week_of', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=2)),
                ('workouts', models.ManyToManyField(to='workouts.Workout')),
            ],
        ),
    ]
