from rest_framework import serializers

from core.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_Fields = ('id',)


class IngredientSerializer(serializers.Serializer):
    """Serializer for ingredient objects"""

    class meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_Fields = ('id',)
