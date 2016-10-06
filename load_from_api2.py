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

movie_id_list = [342473, 347026]

# OTHERS

movies = tmdb.Movies().upcoming()
db_movies = Movie.objects.all()

db_ids = []

for db_movie in db_movies:
    db_ids.append(db_movie.tmdb_id)

results = movies['results']

for movie in results:
    data, created = Movie.objects.update_or_create(tmdb_id=movie['id'], 
                                                   defaults={'title':movie['title'],
                                                             'release':movie['release_date'],
                                                             'description':movie['overview'],
                                                             'backdrop':movie['backdrop_path'],
                                                             'poster':movie['poster_path'],
                                                             'popularity':movie['popularity']})
    if created:
        genres = []
        crew = []
        cast = []
        genres = movie['genre_ids']
        for gnre in genres:
            data.genre.add(gnre)
        mvie = tmdb.Movies(movie['id'])
        info = mvie.info()
        vids = mvie.videos()
        trailers = vids['results']
        for trailer in trailers:
            trailer, created = Trailer.objects.update_or_create(link=trailer['key'], trailer_title=trailer['name'], movie=data)
        credits = mvie.credits()
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
    else:
        pass


for db_movie in db_movies:
    dbmv = tmdb.Movies(db_movie.tmdb_id)
    info = dbmv.info()
    vids = dbmv.videos()
    trailers = vids['results']
    for trailer in trailers:
        trailer, created = Trailer.objects.get_or_create(link=trailer['key'], trailer_title=trailer['name'], movie=db_movie)