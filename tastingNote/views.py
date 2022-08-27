import os
import logging
from datetime import datetime
import hashlib
import time
import base64

import CONSTANT as CONST
from utils.logger import get_initialized_logger
from .models import Imagemeta
from .serializer import ImagemetaSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.

logger = get_initialized_logger("tastingNote logger", logging.INFO, os.path.join(CONST.LOG_ROOT_DIR, "tastingNote.log"))


@api_view(['GET', 'POST', 'OPTIONS'])
def metadata(request):
    logger.info(datetime.now())
    logger.info(request)

    if request.method == "GET":
        logger.info("GET REQUEST")
        image_metad_list = Imagemeta.objects.all().order_by("-id")
        serializer = ImagemetaSerializer(image_metad_list, many=True)
        return HttpResponse(content=serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST" or request.method == "OPTIONS":
        logger.info("POST REQUEST")
        logger.info(request.headers)
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
        image_file_save_path = os.path.join(CONST.IMAGE_FILE_DIR_FOR_TASTING_NOTE, f"{file_name}.{file_extension}")
        logger.info(f"image_file_save_path: {image_file_save_path}")
        img_file = open(image_file_save_path, 'wb')
        img_file.write(decoded_data)
        img_file.close()

        upload_date = datetime.now().replace(microsecond=0)
        upload_date.astimezone(CONST.KST)
        insert_data = {"datetime": upload_date, "image_file_name": f"{file_name}.{file_extension}"}
        serializer = ImagemetaSerializer(Imagemeta(), data=insert_data)
        header = {"Access-Control-Allow-Origin": "http://localhost:19006"}
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Image meta saved! image: {file_name}")
            return HttpResponse(content=serializer.data, status=status.HTTP_200_OK, headers=header)

        return HttpResponse(content=serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers=header)