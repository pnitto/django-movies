# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pandas as pd
from app1.models import Movie

def load_movie(apps, schema_editor):
    movie_data = pd.read_csv('ml-1m/movies.dat', names=["id", "movie_title", "genres"], encoding="windows-1252", sep="::")
    for movie in movie_data.iterrows():
        movie_obj = movie[1]
        Movie.objects.create(id=movie_obj.id, movie_title=movie_obj.movie_title, genres=movie_obj.genres)




class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20150701_1236'),
    ]

    operations = [
        migrations.RunPython(load_movie)
    ]
