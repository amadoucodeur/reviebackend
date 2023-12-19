from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ArticleListSerializer, ArticleDetailSerializer, CategotyListSerialiser
from .models import Article, Category


class CayegoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategotyListSerialiser
    queryset = Category
    

class ArticleViewset(ReadOnlyModelViewSet):
    serializer_class = ArticleListSerializer
    detail_serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()




# Create your views here.
