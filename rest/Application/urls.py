from django.urls import path
from .views import article_list, article_detail, ArticleAPIView

urlpatterns = [
    # path('article/', article_list, name='article'),
    path('article/', ArticleAPIView.as_view(), name='article'),
    path('detail/<str:pk>/', article_detail, name='article_detail'),
]