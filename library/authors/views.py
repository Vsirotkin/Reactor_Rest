from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Biography, Article
from .serializers import AuthorSerializer, BookSerializer, BiographySerializer, ArticleSerializer

from rest_framework.renderers import AdminRenderer

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.settings import api_settings


class AuthorModelViewSet(ModelViewSet):
    #renderer_classes = ['StaticHTMLRenderer']
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BiographyModelViewSet(ModelViewSet):
    # renderer_classes = [AdminRenderer] changeble view
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
