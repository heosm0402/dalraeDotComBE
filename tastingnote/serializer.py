from rest_framework import serializers
from .models import Imagemeta


class ImagemetaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField()
    image_file_name = serializers.CharField()

    class Meta:
        model = Imagemeta
        field = ["id", "date", "image_file_name"]
