# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_rater_postal_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rater',
            name='user',
        ),
    ]
