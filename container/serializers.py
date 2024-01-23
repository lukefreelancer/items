from rest_framework import serializers
from .models import Container
from structure.models import Structure
class ContainerSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    x_position = serializers.CharField()
    y_position = serializers.CharField()
    items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    structure = serializers.PrimaryKeyRelatedField(queryset=Structure.objects.all(),
                                                  many=False, required=False)
    def create(self, validated_data):
        return Container.objects.create(**validated_data)

    def update(self, validated_data, id):
        a = Container.objects.get(pk=id)
        a.title=validated_data["title"] or a.title
        structure = Structure.objects.get(pk=validated_data["structure"])
        a.structure= structure
        a.save()
        return a

    def delete(self, validated_data):
        snippet = Container.objects.get(pk=1)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
