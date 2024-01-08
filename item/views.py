from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema

class ItemView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        tasks = Item.objects.all()
        serializer = ItemSerializer(tasks, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ItemSerializer)
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)