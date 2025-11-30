from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book

# -------------------------------------------------------
# Book Serializer
# -------------------------------------------------------
# - Serializes ALL fields from Book
# - Includes custom validation to prevent future years
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

    # Custom validation
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# -------------------------------------------------------
# Author Serializer (with nested books)
# -------------------------------------------------------
# - Serializes author's name
# - Includes nested BookSerializer
# - 'many=True' because one author → many books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]