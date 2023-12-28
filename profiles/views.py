from profiles.models import Profile
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import ProfilePremissions
from .serializers import ProfileSerializer
from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ProfilePremissions]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
    



    