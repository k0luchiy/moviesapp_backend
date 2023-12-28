from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from profiles.models import Profile

from .models import Movie, MovieInteraction
from .serializers import MovieSerializer, MovieInteractionSerializer
from .permissions import IsAdminOrReadOnly, IsOwner

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]

class MovieInteractionViewSet(ModelViewSet):
    # queryset = MovieInteraction.objects.all()
    serializer_class = MovieInteractionSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        profile = get_object_or_404(Profile,user=self.request.user)
        return MovieInteraction.objects.filter(profile=profile)

    def create(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        serializer = MovieInteractionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profile=profile)
        return Response(serializer.data)
