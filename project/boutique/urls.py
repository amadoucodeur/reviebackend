from rest_framework import routers
from .views import ArticleViewset, CayegoryViewset
from django.urls import path, include


router = routers.SimpleRouter()

router.register('articles',ArticleViewset, basename='articles')
router.register('category',CayegoryViewset, basename='category')


urlpatterns = [
    path('',include(router.urls))
]