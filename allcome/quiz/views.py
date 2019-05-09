from rest_framework.viewsets import ModelViewSet
from .models import QuizModel
from .serializers import QuizSerializer


class QuizViewSet(ModelViewSet):
    queryset = QuizModel.objects.all()
    serializer_class = QuizSerializer


