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
