from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Structure
from .serializers import StructureSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema

class StructureView(APIView):

    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        tasks = Structure.objects.all()
        serializer = StructureSerializer(tasks, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=StructureSerializer)
    def post(self, request):
        serializer = StructureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
