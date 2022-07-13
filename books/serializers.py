# Serializers for the Book API View
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # Serializer for Book object
    author = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='display_name')
    likes = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='display_name')

    class Meta:
        model = Book()
        fields = ['title', 'author', 'id', 'likes', 'no_of_likes']

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
