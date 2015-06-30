from django.db import models

class Rater(models.Model):
    user_id = models.IntegerField()
    user_age = models.IntegerField()

class Movies(models.Model):
    movie_title = models.TextField(max_length=50)
    movie_id = models.IntegerField()

    def __str__(self):
        return self.movie_title

class Ratings(models.Model):
    movie_rating = models.IntegerField()
