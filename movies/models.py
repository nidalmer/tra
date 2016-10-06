from django.db import models
from datetime import date
from django.utils.safestring import mark_safe
import math

class Genre(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.genre

    def get_movies_display(self):
        result = ""
        for movie in self.movie_set.all():
            result += "{}".format(movie.get_poster_html())
        return mark_safe(result)


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def get_movies_display(self):
        result = ""
        for movie in self.directed_movies.all():
            result += "{}".format(movie.get_poster_html())
        for movie in self.acted_movies.all():
            result += "{}".format(movie.get_poster_html())
        return mark_safe(result)


class Movie(models.Model):
    title = models.CharField(max_length=511)
    tmdb_id = models.IntegerField(null=True, blank=True, unique=True)
    release = models.DateField(null=True, blank=True)
    poster = models.TextField(max_length=500, null=True)
    backdrop = models.TextField(max_length=500, null=True, blank=True)
    popularity = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    edit = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_released = models.BooleanField(default=False)
    director = models.ManyToManyField(Person, related_name="directed_movies")
    actors = models.ManyToManyField(Person, related_name="acted_movies")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return "{} ({})".format(self.title, self.release.year)

    def get_poster_html(self):
        return mark_safe("<img src='{}' height='340'/>".format(self.poster))

    def get_html_stars(self):
        result = ""
        rating = self.imdb_score / 2
        int_part = math.floor(rating)
        for i in range(0, int_part):
            result += "<span class='fa fa-star'></span>"
        if (rating - int_part) >= 0.5:
            result += "<span class='fa fa-star-half-o'></span>"
        else:
            result += "<span class='fa fa-star-o'></span>"
        for i in range(1, 5 - int_part):
            result += "<span class='fa fa-star-o'></span>"
        result = "<span class='star{}'>{}</span>".format(int_part, result)
        return mark_safe(result)

    def was_released(self):
        if date.today() > self.release:
            return True
        return False


class Trailer(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    trailer_title = models.CharField(max_length=1000, null=True, blank=True)
    link = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.movie) + ':' + self.link
