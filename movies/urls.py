from django.conf.urls import url
from . import views

urlpatterns = [
    # /movies/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /movies/movie_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /movies/genre_id/
    url(r'^genre/(?P<pk>[0-9]+)/$', views.GenreView.as_view(), name='genre'),
    # /movies/poular/
    url(r'^popular/$', views.PopularView.as_view(), name='popular'),
]
