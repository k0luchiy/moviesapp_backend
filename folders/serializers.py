from rest_framework.serializers import ModelSerializer

from .models import Folder

class FolderSerializer(ModelSerializer):

    class Meta:
        model = Folder
        fields = [
            'id',
            # 'profile',
            'title',
            'description',
            'movies_id',
        ]
        read_only_fields = ["id"]
        # extra_kwargs = {
        #     'profile': {'write_only': True},
        # }

    