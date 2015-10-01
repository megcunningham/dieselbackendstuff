# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseSet',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('number_of_sets', models.CharField(max_length=2)),
                ('weight', models.CharField(blank=True, max_length=40)),
                ('reps', models.CharField(blank=True, max_length=20)),
                ('notes', models.CharField(blank=True, max_length=200)),
                ('exercise', models.ForeignKey(to='workouts.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('group_name', models.CharField(unique=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('workout_name', models.CharField(unique=True, max_length=60)),
                ('exercise', models.ManyToManyField(to='workouts.ExerciseSet')),
                ('group_name', models.ForeignKey(to='workouts.MuscleGroup')),
            ],
        ),
    ]
