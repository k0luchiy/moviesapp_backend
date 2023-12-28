from django.db import models
from PIL import Image

from profiles.models import Profile

class Movie(models.Model):
    title = models.CharField(default="",max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    rating = models.DecimalField(blank=True, null=True, max_digits=2, decimal_places=1)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    length = models.PositiveSmallIntegerField(blank=True, null=True)
    director_name = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    age_rating = models.PositiveSmallIntegerField(blank=True, null=True)
    countries = models.CharField(max_length=100, blank=True, null=True)
    poster = models.ImageField(default="undefiend_poster.jpg", upload_to="posters_images/")

    def save(self, *args, **kwargs):
        super(Movie, self).save(*args, **kwargs)
        image = Image.open(self.poster.path)
        IMAGE_WIDTH = 300
        IMAGE_HEIGHT = 500
        
        if image.width > IMAGE_WIDTH or image.height > IMAGE_HEIGHT:
            image.thumbnail((IMAGE_WIDTH, IMAGE_HEIGHT))
            image.save(self.poster.path)

class MovieInteraction(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False, blank=True)
    watched = models.BooleanField(default=False, blank=True)
    comment = models.CharField(max_length=150, blank=True, null=True)
