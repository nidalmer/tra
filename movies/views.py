from django.views import generic
from django.db.models import Max, Q
from el_pagination.views import AjaxListView
from .models import Movie, Genre, Person


class IndexView(AjaxListView):
    template_name = 'movies/index.html'
    page_template = 'movies/all_movies.html'
    context_object_name = 'all_movies'
    model = Movie

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'all_genres': Genre.objects.all(),
            'our_pick': Movie.objects.get(pk=100),
            'page_title': 'Latest'
        })
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Movie.objects.filter(Q(title__icontains=query) |
                                        Q(release__icontains=query) |
                                        Q(director__name__icontains=query) |
                                        Q(actors__name__icontains=query)
                                        ).distinct()
        else:
            return Movie.objects.annotate(Max("trailer__date")).order_by('-trailer__date__max')


class PopularView(AjaxListView):
    template_name = 'movies/index.html'
    page_template = 'movies/all_movies.html'
    context_object_name = 'all_movies'
    model = Movie

    def get_context_data(self, **kwargs):
        context = super(PopularView, self).get_context_data(**kwargs)
        context.update({
            'all_genres': Genre.objects.all(),
            'our_pick': Movie.objects.order_by('-popularity').first(),
            'page_title': 'Popular'
        })
        return context

    def get_queryset(self):
        return Movie.objects.all().order_by('-popularity')


class DetailView(generic.DetailView):
    model = Movie
    template_name = 'movies/detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context.update({
            'all_genres': Genre.objects.all()
        })
        return context


class GenreView(generic.DetailView):
    model = Genre
    template_name = 'movies/genre.html'
    page_template = 'movies/all_movies.html'
    context_object_name = 'this_genre'

    def get_context_data(self, **kwargs):
        context = super(GenreView, self).get_context_data(**kwargs)
        context.update({
            'all_movies': Movie.objects.all().filter(genre=self.object),
            'all_genres': Genre.objects.all(),
            'our_pick': Movie.objects.filter(genre=self.object).order_by('-popularity').first()
        })
        return context
