from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ArticleListSerializer, ArticleDetailSerializer, CategotyListSerialiser
from .models import Article, Category
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


class CayegoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategotyListSerialiser
    queryset = Category
    

class ArticleViewset(ReadOnlyModelViewSet):
    serializer_class = ArticleListSerializer
    detail_serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()
    # permission_classes = [IsAuthenticated]


class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return Response({"detail": "Compte créé avec succès"}, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return Response({"detail": "Connexion réussie"}, status=status.HTTP_200_OK)
        else:
            return Response(form.errors, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"detail": "Déconnexion réussie"}, status=status.HTTP_200_OK)


class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return Response({"detail": "Compte supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)
# Create your views here.
