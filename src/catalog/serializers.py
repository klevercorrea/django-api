from rest_framework import serializers
from catalog.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'books')
        extra_kwargs = {'books': {'required': False}}


class BookSerializer(serializers.ModelSerializer):

    authors = AuthorSerializer(many=True, read_only=True)

    human_readable_authors = serializers.SerializerMethodField()

    def get_human_readable_authors(self, book):
        return ', '.join([author.name for author in book.authors.all()])

    class Meta:
        model = Book
        fields = ('id', 'name', 'description',
                  'authors', 'human_readable_authors')
        extra_kwargs = {'authors': {'required': False}}
