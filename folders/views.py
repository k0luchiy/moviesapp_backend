from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from profiles.models import Profile

from .models import Folder
from .serializers import FolderSerializer
from .permissions import IsOwner

class FolderViewSet(ModelViewSet):
    # queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        profile = get_object_or_404(Profile, user=self.request.user)
        return Folder.objects.filter(profile=profile)
    
    def create(self, request):
        profile = get_object_or_404(Profile,user=request.user)
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profile=profile)
        return Response(serializer.data)