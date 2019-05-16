from rest_framework.viewsets import ModelViewSet
from .models import QuizModel
from .serializers import QuizSerializer
from django_filters.rest_framework import DjangoFilterBackend


class QuizViewSet(ModelViewSet):
    queryset = QuizModel.objects.all()
    serializer_class = QuizSerializer


class QuizRequestViewSet(ModelViewSet):
    queryset = QuizModel.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        subject = self.request.query_params.get('subject',None)
        if subject is not None:
            subject_qs = qs.filter(subject=subject)
            return subject_qs.order_by("?")[:1]