# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_auto_20151001_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciseset',
            name='group_name',
            field=models.ManyToManyField(to='workouts.MuscleGroup'),
        ),
    ]
