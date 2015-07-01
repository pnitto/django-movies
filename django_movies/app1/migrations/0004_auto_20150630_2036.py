# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pandas as pd

from django.db import models, migrations

def load_movie_data(apps, schema_editor):
    movie_data = pd.read_csv('movies.dat', names=["id", "genres","movie_title"])

    for row in movie_data.iterrows():
        movie_title = row[1]



class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20150630_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_id',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='user_age',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='user_id',
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie',
            field=models.ForeignKey(default=0, to='app1.Rater'),
        ),
        migrations.AddField(
            model_name='rater',
            name='age',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='rater',
            name='gender',
            field=models.CharField(default='m', max_length=10),
        ),
        migrations.AddField(
            model_name='rater',
            name='occupation',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='rater',
            name='user',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(default=None, to='app1.Rater'),
        ),
    ]
