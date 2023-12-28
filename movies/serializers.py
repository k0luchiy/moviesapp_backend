from rest_framework import serializers

from .models import Movie, MovieInteraction

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "rating",
            "year",
            "length",
            "director_name",
            "genre",
            "age_rating",
            "countries",
            "poster",
        ]
        read_only_fields = ["id"]

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie

class MovieInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieInteraction
        fields = ["movie", "liked", "watched", "comment"]