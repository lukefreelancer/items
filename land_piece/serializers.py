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

    def update(self, validated_data, id):
        a = Item.objects.get(pk=id)
        a.title=validated_data["title"] or a.title
        # structures = Structure.objects.get(pk=validated_data["structure"])
        # a.structure= structure
        a.save()
        return a

    def delete(self, validated_data):
        snippet = LandPiece.objects.get(pk=1)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
