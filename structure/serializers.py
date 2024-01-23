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

    def update(self, validated_data, id):
        a = Structure.objects.get(pk=id)
        a.title = validated_data["title"] or a.title
        land_piece = LandPiece.objects.get(pk=validated_data["land_piece"])
        a.land_piece = land_piece
        a.save()
        return a

    def delete(self, validated_data):
        snippet = Structure.objects.get(pk=1)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
