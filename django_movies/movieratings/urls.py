"""django_movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout
from django.core.urlresolvers import reverse_lazy
from app1.views import top_20_movies
from app1.views import rater_detail
from app1.views import movie_detail
from app1.views import movie_list
from app1.views import create_rating
from app1.views import user_registration


urlpatterns = [
    url(r'^$', movie_list, name="movie_list"),
    url(r'^accounts/login/',login, name="login"),
    url(r'^logout/', logout, {'next_page': '/'}, name="logout"),
    url(r'^toptwenty/', top_20_movies, name="top_20_movies"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rater-detail/(?P<user_id>\d+)/$', rater_detail, name="rater_detail"),
    url(r'^movie-detail/', movie_detail, name="movie_detail"),
    url(r'^registration/', user_registration, name="user_registration"),
    url(r'^create-rating/$',create_rating, name="create_rating")
]  #(?P<id>\d+)/$'
