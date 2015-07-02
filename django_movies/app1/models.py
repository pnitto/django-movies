from django.db import models

class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.IntegerField()
    postal_code = models.CharField(max_length=30)

    def __str__(self):
        return"{}-{}-{}".format(self.age, self.gender, self.occupation)

class Movie(models.Model):
    movie_title = models.TextField(max_length=100)
    genres = models.CharField(max_length=200, default=0)

    def __str__(self):
        return self.movie_title

    @property
    def average_rating(self):
        movie_ratings = [rating.movie_rating for rating in Rating.objects.filter(movie=self)]
        return movie_ratings

    @property
    def genres_list(self):
        return self.genres.split('|')


class Rating(models.Model):
    user = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    movie_rating = models.IntegerField()

