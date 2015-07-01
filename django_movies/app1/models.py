from django.db import models

class Rater(models.Model):
    user = models.IntegerField(default = None)
    age = models.IntegerField(default = None)
    gender = models.CharField(max_length=10,default='m')
    occupation = models.CharField(max_length=20,default=None)

    def __str__(self):
        return"{}-{}-{}-{}".format(self.user,self.age, self.gender, self.occupation)

class Movie(models.Model):
    movie_title = models.TextField(max_length=50)
    movie = models.ForeignKey(Rater,default=0)
    genres = models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.movie_title

class Rating(models.Model):
    user = models.ForeignKey(Rater,default=None)
    movie_rating = models.IntegerField()

