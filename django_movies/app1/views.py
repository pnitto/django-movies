from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render_to_response
from app1.models import Movie, Rater, Rating
from statistics import mean
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from app1.forms import RatingForm


def user_registration(request):
    if request.POST:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_form = UserCreationForm({
            'username': username,
            'password1': password1,
            'password2': password2,
        })
        try:
            user_form.save(commit=True)
            return HttpResponseRedirect("/")
        except ValueError:
            return render_to_response("registration/create_user.html",
                              {'form': user_form},
                              context_instance=RequestContext(request))


    return render_to_response("registration/create_user.html",
                              {'form': UserCreationForm()},
                              context_instance=RequestContext(request))

@login_required
def top_20_movies(request):
    context = {}
    ratings_dict = {}
    all_movies = Movie.objects.all()[:10]

    for movie_obj in all_movies:
        all_rating = [rating.movie_rating for rating in Rating.objects.filter(movie=movie_obj)]

        if all_rating:
            mean_rating = mean(all_rating)
            ratings_dict[movie_obj.movie_title] = mean_rating

    context = {"movie_list": ratings_dict.items()}
    return render_to_response('top_twenty.html', context, context_instance=RequestContext(request))

#@login_required
def rater_detail(request, user_id):
    rater = Rater.objects.get(id=user_id)
    if request.POST:
        print("It posted!", request.POST)
        request.POST['rater'] = request.user
        form = RatingForm(request.POST)
        form.save()
        context = {"rater" : rater, "form" : form}
        return render_to_response("rater_detail.html",context,context_instance=RequestContext(request))

    form = RatingForm()
    context = {"rater" : rater, "form" : form}
    return render_to_response("rater_detail.html",context,context_instance=RequestContext(request))

@login_required
def movie_detail(request):
    movie = Rating.objects.all()[:10]
    context = {"movie_info": movie}
    return render_to_response("movie_detail.html", context, context_instance=RequestContext(request))

def movie_list(request):
    list_of_movies = Movie.objects.all().order_by('movie_title')[:10]
    context = {"movies": list_of_movies}
    return render_to_response("list_movies.html", context, context_instance=RequestContext(request))

def create_rating(request):
    pass
