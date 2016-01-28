# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_auto_20151209_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('group_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='completeset',
            name='group_name',
            field=models.ForeignKey(to='workouts.MuscleGroup'),
        ),
        migrations.AlterField(
            model_name='exercisename',
            name='group_name',
            field=models.ForeignKey(to='workouts.MuscleGroup'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='group_name',
            field=models.ForeignKey(to='workouts.MuscleGroup'),
        ),
    ]
