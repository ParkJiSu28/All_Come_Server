from .models import QuizModel
from rest_framework.serializers import ModelSerializer


class QuizSerializer(ModelSerializer):
    class Meta:
        model = QuizModel
        fields = '__all__'

