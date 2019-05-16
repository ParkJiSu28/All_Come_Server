from rest_framework.viewsets import ModelViewSet
from .models import QuizModel
from .serializers import QuizSerializer
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class QuizViewSet(ModelViewSet):
    queryset = QuizModel.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']


class QuizRequestAPIView(ListAPIView):
    serializer_class = QuizSerializer

