from django.urls import path, include
from .views import ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter # can be used to display the list of routes only can be used with view set classes

router = DefaultRouter()
router.register('article',ArticleViewSet, basename='article')
router.register('art',ArticleViewSet, basename='art')

urlpatterns = [
    # path('article/', article_list, name='article'),
    # path('detail/<str:pk>/', article_detail, name='article_detail'),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>',include(router.urls)),
    path('article/', ArticleAPIView.as_view(), name='article'),
    path('detail/<str:id>/',ArticleDetails.as_view(), name='detail'),
    path('generic/article/<str:id>', GenericAPIView.as_view(), name='generic-article'),
]