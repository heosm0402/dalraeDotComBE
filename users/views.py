import sys
from datetime import datetime

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status

from .serializer import UserSerializer
from .models import User


@api_view(['GET', 'POST'])
def users(request):
    if request.method == "GET":
        user_list = User.objects.all()
        serializer = UserSerializer(user_list, many=True)
        return HttpResponse(content=serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        name = data.get("name")
        print(name)
        birth = datetime.strptime(data.get("birth"), "%y%m%d")
        # data["name"] = name.encode("utf8")
        data["birth"] = birth.date()

        serializer = UserSerializer(User(), data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(content=serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
