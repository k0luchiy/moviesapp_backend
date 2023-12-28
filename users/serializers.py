from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from profiles.models import Profile

class CustomUserSerializer(serializers.ModelSerializer):
    # token = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ["id", "username", "password", "email"]
        read_only_fields = ["id"]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        # user = CustomUser.objects.create(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()

        Profile.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance
    
    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
