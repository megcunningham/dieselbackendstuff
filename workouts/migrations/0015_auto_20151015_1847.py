# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0014_auto_20151015_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='level',
            field=models.ForeignKey(default=0, to='workouts.DifficultyLevel'),
            preserve_default=False,
        ),
    ]
