from __future__ import unicode_literals
from django.db import models, migrations
import pandas as pd
from app1.models import Rater, Movie, Rating


def load_ratings(apps, schema_editor):
    rating_data = pd.read_csv('ml-1m/ratings.dat', names=["rater_id", "movie_id", "rating","timestamp"], encoding="windows-1252", sep="::")
    for rating in rating_data.iterrows():
        rating_obj = rating[1]
        movie = Movie.objects.get(id=rating_obj.movie_id)
        rater = Rater.objects.get(id=rating_obj.rater_id)
        Rating.objects.create(movie=movie,
                             user=rater,
                             movie_rating=rating_obj.rating,
        )
        print("Creating ratings!")



class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20150701_2027'),
    ]

    operations = [
        migrations.RunPython(load_ratings)
    ]
