import os
import logging
import base64
import hashlib
import time
from datetime import datetime

import CONSTANT as CONST
from utils.logger import get_initialized_logger

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


logger = get_initialized_logger("reply logger", logging.INFO, os.path.join(CONST.LOG_ROOT_DIR, "studio.log"))


# Create your views here.
@api_view(['GET', 'POST', 'OPTIONS'])
def image(request):
    logger.info(datetime.now())
    logger.info(request.headers)
    if request.method == "GET":
        return HttpResponse(content="get image", status=status.HTTP_200_OK)
    elif request.method == "POST" or request.method == "OPTIONS":
        try:
            logger.info("POST REQUEST")
            if request.data.get("expo_image_upload"):
                image_uri = request.data.get("expo_image_upload")
                file_name = hashlib.sha256(str(time.time()).encode('utf-8')).hexdigest()
                file_meta_data, encoded_image_data = image_uri.split(",")
                file_extension = file_meta_data.split("/")[-1].split(";")[0]
            else:
                file_name = request.data.get("attached_file_name").split(".")[0]
                file_extension = request.data.get("attached_file_type").split("/")[-1]
                encoded_image_data = request.data.get("attached_file_uri")

            logger.info(f"file name: {file_name}")
            logger.info(f"file extension: {file_extension}")
            decoded_data = base64.b64decode(encoded_image_data)
            img_file = open(os.path.join(CONST.IMAGE_FILE_ROOT_DIR, f"{file_name}.{file_extension}"), 'wb')
            img_file.write(decoded_data)
            img_file.close()
            response_data = {"message": "posting image done"}
        except Exception as e:
            logger.exception(e)

        return HttpResponse(content=response_data, status=status.HTTP_200_OK)
