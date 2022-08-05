from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    sex = serializers.CharField()
    birth = serializers.DateField()

    class Meta:
        model = User
        fields = ["id", "name", "sex", "birth"]
