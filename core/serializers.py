from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """Сериализатор автора."""

    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    """Сериализатор книги."""
    author = AuthorSerializer(
        read_only=True
    )  # Для удобства отражения вложенных данных
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        write_only=True,
        source="author"
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "author",
            "author_id",
            "title",
            "publication_year",
            "preface",
            "cover_image"
        ]