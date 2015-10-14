# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0012_auto_20151014_2029'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exercise',
            new_name='ExerciseName',
        ),
    ]
