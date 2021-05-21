from django.urls import path
from .views import ArticleAPIView, ArticleDetails, GenericAPIView

urlpatterns = [
    # path('article/', article_list, name='article'),
    # path('detail/<str:pk>/', article_detail, name='article_detail'),
    path('article/', ArticleAPIView.as_view(), name='article'),
    path('detail/<str:id>/',ArticleDetails.as_view(), name='detail'),
    path('generic/article/<str:id>', GenericAPIView.as_view(), name='generic-article'),
]