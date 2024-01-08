from rest_framework import serializers
from .models import LandPiece
class LandPieceSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    x_position = serializers.CharField()
    y_position = serializers.CharField()
    structures = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    def create(self, validated_data):
        return LandPiece.objects.create(**validated_data)
