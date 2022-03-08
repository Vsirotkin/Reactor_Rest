from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Biography, Artical
from .serializers import AuthorModelSerializer, BookModelSerializer, BiographyModelSerializer, ArticalModelSerializer


class AuthorModelViewSet(ModelViewSet):
    #renderer_classes = ['StaticHTMLRenderer']
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class ModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Artical.objects.all()
    serializer_class = ArticalModelSerializer
