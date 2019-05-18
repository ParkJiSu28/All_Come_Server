from django.urls import path, include, re_path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user_list', views.UserViewSet)
router.register('book_list', views.BookmarkViewSet)


urlpatterns = [
    path('', include(router.urls)),
    #re_path(r'^bookmark/$', views.BookmarkViewSet, name='index'),
]



#from django.urls import path
#from . import views

#email_list = views.UserViewSet.as_view({
#    'get':'list',
#    'put' :'update',
#    'post': 'create',
#    'delete': 'destroy',
#})


#bookmark_list = views.BookmarkViewSet.as_view({
#    'get':'list',
#})


#urlpatterns = [
#    path('user_list', email_list),
#    path('bookmark', bookmark_list),
#]