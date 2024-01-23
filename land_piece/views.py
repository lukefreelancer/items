from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LandPiece
from .serializers import LandPieceSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

class LandPieceView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [IsAuthenticated]

    def get(self, request):
        id = request.query_params.get('id')
        if id:
            result = LandPiece.objects.get(pk=id)
            serializer = LandPieceSerializer(result)
        else:
            result = LandPiece.objects.all()
            serializer = LandPieceSerializer(result, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=LandPieceSerializer)
    def post(self, request):
        serializer = LandPieceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=LandPieceSerializer)
    def put(self, request):
        serializer = LandPieceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(serializer.data, request.data["id"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=LandPieceSerializer)
    def delete(self, request):
        snippet = LandPiece.objects.get(pk=request.data["id"])
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
