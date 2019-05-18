from rest_framework.serializers import ModelSerializer
from .models import User, Bookmark


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BookmarkSerializer(ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'