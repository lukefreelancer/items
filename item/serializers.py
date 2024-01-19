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


    def update(self, validated_data):
        return Item.objects.filter(pk=2 or name="pizza").update(name="pizza1")
