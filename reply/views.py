import json
import logging
import os.path
from datetime import datetime, timedelta

import CONSTANT as CONST
from utils.logger import get_initialized_logger
from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .serializer import ReplySerializer
from .models import Reply


logger = get_initialized_logger("reply logger", logging.INFO, os.path.join(CONST.LOG_ROOT_DIR, "reply.log"))


@api_view(['GET', 'POST', 'OPTIONS'])
def reply(request):
    if request.method == "GET":
        logger.info("GET REQUEST")
        reply_list = Reply.objects.all().order_by("-id")
        serializer = ReplySerializer(reply_list, many=True)
        return HttpResponse(content=json.dumps(serializer.data), status=status.HTTP_200_OK)

    elif request.method == "POST" or request.method == "OPTIONS":
        logger.info("POST REQUEST")
        data = JSONParser().parse(request)
        date = datetime.now().replace(microsecond=0)
        date.astimezone(CONST.KST)
        data["date"] = date

        serializer = ReplySerializer(Reply(), data=data)
        header = {"Access-Control-Allow-Origin": "http://localhost:19006"}
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Reply saved! Data: {data}")
            return HttpResponse(content=serializer.data, status=status.HTTP_200_OK, headers=header)
        print(serializer.errors)
        return HttpResponse(content=serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers=header)
