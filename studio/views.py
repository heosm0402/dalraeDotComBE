import os
import logging
import base64

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
    # print(request.data)
    if request.method == "GET":
        return HttpResponse(content="get image", status=status.HTTP_200_OK)
    elif request.method == "POST" or request.method == "OPTIONS":
        try:
            logger.info("POST REQUEST")
            file_metadata, encoded_image_data = request.data.get("file_attachment").split(",")
            image_extension = file_metadata.split("/")[-1].split(";")[0]
            decoded_data = base64.b64decode(encoded_image_data)
            img_file = open(os.path.join(CONST.IMAGE_FILE_ROOT_DIR, f"image.{image_extension}"), 'wb')
            img_file.write(decoded_data)
            img_file.close()

        except Exception as e:
            logger.exception(e)

        return HttpResponse(content="post image", status=status.HTTP_200_OK)
