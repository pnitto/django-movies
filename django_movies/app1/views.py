from django.shortcuts import render_to_response
from app1.models import Movie, Rater, Rating



    # Movie.object.get


#possibly bring in movie and movie_rating
def top_20_movies(request):
    all_movies = list(Rating.movie_rating.get())
    for movies in all_movies:
        top_movies = all_movies.order_by(10:)
    context = {"all_movies": all_movies}
    return render_to_response('top_twenty.html', context)
#get all movies, and only keep the highest movie ratings

