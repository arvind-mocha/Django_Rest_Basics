from django.urls import path
from .views import ArticleAPIView, ArticleDetails

urlpatterns = [
    # path('article/', article_list, name='article'),
    # path('detail/<str:pk>/', article_detail, name='article_detail'),
    path('article/', ArticleAPIView.as_view(), name='article'),
    path('detail/<str:id>/',ArticleDetails.as_view(), name='detail')
]