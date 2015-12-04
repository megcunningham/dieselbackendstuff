# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompleteSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=20)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DifficultyLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.CharField(default='Beginner', unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=20)),
                ('name', models.CharField(unique=True, max_length=75)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NumberOfSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('set_number', models.CharField(max_length=30)),
                ('weight', models.CharField(blank=True, max_length=30)),
                ('reps', models.CharField(blank=True, max_length=30)),
                ('exercise_set', models.ForeignKey(to='workouts.CompleteSet')),
            ],
        ),
        migrations.CreateModel(
            name='Split',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('days', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyWorkout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('week_of', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=20)),
                ('workout_name', models.CharField(unique=True, max_length=60)),
                ('exercise', models.ManyToManyField(to='workouts.CompleteSet')),
                ('level', models.ForeignKey(to='workouts.DifficultyLevel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='split',
            name='week_of',
            field=models.ForeignKey(to='workouts.WeeklyWorkout'),
        ),
        migrations.AddField(
            model_name='split',
            name='workouts',
            field=models.ManyToManyField(to='workouts.Workout'),
        ),
        migrations.AddField(
            model_name='completeset',
            name='exercise',
            field=models.ForeignKey(to='workouts.ExerciseName'),
        ),
    ]
