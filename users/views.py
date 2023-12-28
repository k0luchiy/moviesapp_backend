from rest_framework import viewsets

from .serializers import CustomUserSerializer
from .models import CustomUser
from .permissions import CustomUserPremissions

class CustomUserViewSet(viewsets.ModelViewSet):
    # queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [CustomUserPremissions,]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.pk)