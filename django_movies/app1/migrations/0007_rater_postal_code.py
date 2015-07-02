# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20150701_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='postal_code',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
