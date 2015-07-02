from django.contrib import admin

from app1.models import Rater, Rating, Movie

admin.site.register(Rater)
admin.site.register(Rating)
admin.site.register(Movie)
