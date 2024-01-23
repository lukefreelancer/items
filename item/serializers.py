from rest_framework import serializers
from .models import Item
from container.models import Container
class ItemSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    container = serializers.PrimaryKeyRelatedField(queryset=Container.objects.all(),
                                                  many=False, required=False)
    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, validated_data, id):
        a = Item.objects.get(pk=id)
        a.title=validated_data["title"] or a.title
        container = Container.objects.get(pk=validated_data["container"])
        a.container = container
        a.save()
        return a

    def delete(self, validated_data):
        snippet = Item.objects.get(pk=1)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
