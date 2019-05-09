from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('problem', views.QuizViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
