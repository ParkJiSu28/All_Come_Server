from rest_framework.viewsets import ModelViewSet
from .models import Like
from .serializers import MarkSerializer


class BookmarkViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = MarkSerializer