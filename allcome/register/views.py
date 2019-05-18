from rest_framework.viewsets import ModelViewSet
from .models import User, Bookmark
from .serializers import UserSerializer, BookmarkSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('email',)


class BookmarkViewSet(ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer




