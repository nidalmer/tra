from django.contrib import admin
from .models import Genre, Trailer, Movie, Person


admin.site.register(Genre)
admin.site.register(Trailer)
admin.site.register(Movie)
admin.site.register(Person)
