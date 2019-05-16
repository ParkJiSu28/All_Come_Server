from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #filter_backends = [SearchFilter]
    #search_filedls = ['email']
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('email',)



