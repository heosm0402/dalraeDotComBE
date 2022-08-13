from rest_framework import serializers
from .models import Reply


class ReplySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField()
    name = serializers.CharField()
    content = serializers.CharField()

    class Meta:
        model = Reply
        fields = ["id", "date", "name", "content"]
