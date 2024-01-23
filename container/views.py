from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Container
from .serializers import ContainerSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated


class ContainerView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [IsAuthenticated]

    def get(self, request):
        id = request.query_params.get('id')
        if id:
            result = Container.objects.get(pk=id)
            serializer = ContainerSerializer(result)
        else:
            result = Container.objects.all()
            serializer = ContainerSerializer(result, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ContainerSerializer)
    def post(self, request):
        serializer = ContainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ContainerSerializer)
    def put(self, request):
        serializer = ContainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(serializer.data, request.data["id"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ContainerSerializer)
    def delete(self, request):
        snippet = Container.objects.get(pk=request.data["id"])
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
