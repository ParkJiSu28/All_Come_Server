from django.urls import path, include,re_path
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet,QuizRequestAPIView

router = DefaultRouter()
router.register('problem',QuizViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('request',QuizRequestAPIView.as_view()),
]
