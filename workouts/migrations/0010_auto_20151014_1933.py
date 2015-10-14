# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0009_weeklyworkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Split',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=2)),
                ('workouts', models.ManyToManyField(to='workouts.Workout')),
            ],
        ),
        migrations.RemoveField(
            model_name='weeklyworkout',
            name='day',
        ),
        migrations.RemoveField(
            model_name='weeklyworkout',
            name='workouts',
        ),
        migrations.AddField(
            model_name='weeklyworkout',
            name='split',
            field=models.ForeignKey(to='workouts.Split', default=1),
            preserve_default=False,
        ),
    ]
