from rest_framework import serializers
from .models import Article


# Normal Serializer
# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     author = serializers.CharField(max_length=200)
#     email = serializers.EmailField(max_length=200)
#     date = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('author', instance.email)
#         instance.date = validated_data.get('author', instance.date)

# Model Serializser
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['id','title','author']
        fields = '__all__'