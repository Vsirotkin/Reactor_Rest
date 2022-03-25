#from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
# from rest_framework.serializers import StringRelatedField
from rest_framework.renderers import JSONRenderer

from .models import Author, Article, Book, Biography

class SimpleAuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BiographySerializer(serializers.ModelSerializer):
    author = SimpleAuthorModelSerializer()
    class Meta:
        model = Biography
        fields = ['text', 'author']

class ArticleSerializer(serializers.ModelSerializer):
    author = SimpleAuthorModelSerializer()

    class Meta:
        model = Article
        exclude = ['name']

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'

