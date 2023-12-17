from rest_framework import routers
from .views import ArticleViewset
from django.urls import path, include


router = routers.SimpleRouter()

router.register('articles',ArticleViewset, basename='articles')


urlpatterns = [
    path('',include(router.urls))
]