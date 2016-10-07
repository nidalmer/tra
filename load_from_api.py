#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trailers.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "trailers.settings"
import django
django.setup()
import tmdbsimple as tmdb
from movies.models import Movie, Person, Trailer

tmdb.API_KEY = '822cba76ea391ade520ab8d8a0038ac9'

# MOVIE LIST

movie_id_list = []

movie = tmdb.Movies(movie_id)
info = movie.info()
vids = movie.videos()
credits = movie.credits()
trailers = vids['results']

data, created = Movie.objects.update_or_create(tmdb_id=info['id'], 
                                               defaults={'title':info['title'],
                                               'release':info['release_date'],
                                               'description':info['overview'],
                                               'backdrop':info['backdrop_path'],
                                               'poster':info['poster_path'],
                                               'popularity':info['popularity']})

genres = []
crew = []
cast = []
genre_ids = info['genres']

for genre_id in genre_ids:
    genres.append(genre_id['id'])

for gnre in genres:
    data.genre.add(gnre)

crew = credits['crew']
cast = credits['cast']

for i in range(1, 5):
    try:
        actor = next(item for item in cast if item["order"] == i)
    except:
        pass
    act, created = Person.objects.update_or_create(name=actor['name'])
    data.actors.add(act)

director = next(item for item in crew if item["department"] == "Directing" and item["job"] == "Director")
dir, created = Person.objects.update_or_create(name=director['name'])
data.director.add(dir)

for trailer in trailers:
    trailer, created = Trailer.objects.get_or_create(link=trailer['key'], trailer_title=trailer['name'], movie=data)
