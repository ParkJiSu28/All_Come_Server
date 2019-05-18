from django.urls import path
from . import views


bookmark = views.BookmarkViewSet.as_view({
    ['get','list'],

})

urlpatterns = [
    path('book_mark', bookmark),
]