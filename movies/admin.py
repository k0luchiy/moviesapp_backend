from django.contrib import admin

from .models import Movie, MovieInteraction

admin.site.register(Movie)
admin.site.register(MovieInteraction)