from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


# Create your views here.
@api_view(['GET', 'POST'])
def image(request):
    if request.method == "GET":
        return Response(data="get image", status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = JSONParser().parse(request)

        return Response(data="post image", status=status.HTTP_200_OK)


