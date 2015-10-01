# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_exerciseset_group_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exerciseset',
            name='group_name',
        ),
        migrations.AddField(
            model_name='exerciseset',
            name='group_name',
            field=models.ForeignKey(default=1, to='workouts.MuscleGroup'),
            preserve_default=False,
        ),
    ]
