# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='movie_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rater',
            name='user_age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rater',
            name='user_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='movie_rating',
            field=models.IntegerField(),
        ),
    ]
