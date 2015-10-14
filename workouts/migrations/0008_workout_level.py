# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0007_remove_workout_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='level',
            field=models.ForeignKey(default=1, to='workouts.DifficultyLevel'),
            preserve_default=False,
        ),
    ]
