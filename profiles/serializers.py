from rest_framework import serializers

from .models import Profile
from users.serializers import CustomUserSerializer
from folders.serializers import FolderSerializer



class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    folders = FolderSerializer(many=True, required=False)
    
    class Meta:
        model = Profile
        fields = ["id", "user", "description",
                  "folders", "image"]
        read_only_fields = ["id"]

    def update(self, instance, validated_data):
        user_data = validated_data["user"]
        CustomUserSerializer().update(instance.user, user_data)
        instance.description = validated_data.get("description", instance.description)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance


