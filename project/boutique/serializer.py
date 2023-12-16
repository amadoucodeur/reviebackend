from rest_framework import serializers
from .models import Article, ImageArticle, Category, CustomeUser



class ArticleListSerializer(serializers.ModelSerializer):
    images = serializers.ModelSerializer()

    class Meta:
        model = Article
        fields = ['id', 'name','price','quality','add_date','images']

    def get_images(self, instance):
        queryset = instance.images.all()[0]
        serialiser = ImageArticleSerialiser(queryset, many=True)
        return serialiser.data


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class CategotyListSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']



class CategotyDetailSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ImageArticleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ImageArticle
        fields = '__all__'

