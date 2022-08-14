from datetime import datetime
import json
from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .serializer import ReplySerializer
from .models import Reply


@api_view(['GET', 'POST', 'OPTIONS'])
def reply(request):
    print(request)
    if request.method == "GET":
        reply_list = Reply.objects.all().order_by("-id")
        serializer = ReplySerializer(reply_list, many=True)
        print(type(json.dumps(serializer.data)))
        return HttpResponse(content=json.dumps(serializer.data), status=status.HTTP_200_OK)

    elif request.method == "POST" or request.method == "OPTIONS":
        data = JSONParser().parse(request)
        print(data)
        date = datetime.now().replace(microsecond=0)
        data["date"] = date

        serializer = ReplySerializer(Reply(), data=data)
        header = {"Access-Control-Allow-Origin": "http://localhost:19006"}
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(content=serializer.data, status=status.HTTP_200_OK, headers=header)
        print(serializer.errors)
        return HttpResponse(content=serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers=header)
