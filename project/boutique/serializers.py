from rest_framework import serializers
from .models import Article, ImageArticle, Category, CustomeUser



class ArticleListSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'name','price','quality','add_date','images']
        ordering = ['-add_date']

    def get_images(self, instance):
        first_image = instance.images.first()
        if first_image:
            serialiser = ImageArticleSerializer(first_image)
            return serialiser.data
        return None


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


class ImageArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageArticle
        fields = ['image']

