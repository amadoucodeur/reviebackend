from rest_framework import routers
from .views import ArticleViewset, CayegoryViewset, LoginView
from django.urls import path, include


router = routers.SimpleRouter()

router.register('articles',ArticleViewset, basename='articles')
router.register('category',CayegoryViewset, basename='category')


urlpatterns = [
    path('',include(router.urls)),
    path('login/',LoginView.as_view(), name='loginn'),
]