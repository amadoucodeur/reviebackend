from rest_framework import serializers
from .models import Article, ImageArticle, Category, CustomeUser



class ArticleListSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    # category = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'name','price','quality','add_date','images', 'category']
        ordering = ['-add_date']

    def get_images(self, instance):
        first_image = instance.images.first()
        if first_image:
            serialiser = ImageArticleSerializer(first_image)
            return serialiser.data
        return None

    # def get_category(self, instance):
    #     categorys = instance.category.all()
    #     if categorys:
    #         serialiser = CategotyListSerialiser(categorys, many=True)
    #         category_names = [item['name'] for item in serializer.data]  # Accédez à la propriété 'name' de chaque élément dans la liste
    #         return ', '.join(category_names)  # Convertissez la liste en une chaîne séparée par des virgules
    #     return None


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

