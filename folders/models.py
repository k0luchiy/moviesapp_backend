from django.db import models

from profiles.models import Profile
from movies.models import Movie

class Folder(models.Model):
    profile = models.ForeignKey(Profile, related_name="folders", on_delete=models.CASCADE, null=True)
    title = models.CharField(default="Folder", max_length=50)
    description = models.CharField(max_length=150, blank=True, null=True)
    movies_id = models.ManyToManyField(Movie, blank=True, null=True)
