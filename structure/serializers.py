from rest_framework import serializers
from land_piece.models import LandPiece
from .models import Structure
class StructureSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    x_position = serializers.CharField()
    y_position = serializers.CharField()
    containers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    land_piece = serializers.PrimaryKeyRelatedField(queryset=LandPiece.objects.all(),
                                                  many=False, required=False)
    def create(self, validated_data):
        return Structure.objects.create(**validated_data)
