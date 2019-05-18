from rest_framework.serializers import ModelSerializer
from .models import Like


class MarkSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
