from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Biography, Article
from .serializers import AuthorSerializer, BookSerializer, BiographySerializer, ArticleSerializer


class AuthorModelViewSet(ModelViewSet):
    #renderer_classes = ['StaticHTMLRenderer']
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
