# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
import pandas as pd

def load_movie(apps, schema_editor):
    movie_data = pd.read_csv('movies.dat',names=["id", "movie_title","genres"])
    for row in movie_data.iterrows():
        movie_ob = row[1]
        title = Movie.objects.get(id=movie_ob.movie_title)
        genre = Movie.objects.get()
        Movie.objects.create(id=movie_ob.id, movie_title=movie_ob.movie_title,)


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20150630_2036'),
    ]

    operations = [
        migrations.RunPython(load_movie)
    ]
