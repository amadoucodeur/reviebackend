from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ArticleListSerializer, ArticleDetailSerializer
from .models import Article


class ArticleViewset(ReadOnlyModelViewSet):
    serializer_class = ArticleListSerializer
    detail_serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()

# Create your views here.
