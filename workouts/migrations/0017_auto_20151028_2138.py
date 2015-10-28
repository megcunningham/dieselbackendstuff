# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0016_auto_20151021_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='split',
            old_name='day',
            new_name='days',
        ),
    ]
