from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('email',)



