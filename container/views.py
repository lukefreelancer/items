from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Container
from .serializers import ContainerSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema


class ContainerView(APIView):

    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        tasks = Container.objects.all()
        serializer = ContainerSerializer(tasks, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ContainerSerializer)
    def post(self, request):
        serializer = ContainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
