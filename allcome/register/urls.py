from django.urls import path, include, re_path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user_list', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]


