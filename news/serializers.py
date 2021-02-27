from rest_framework import serializers
from news.models import News, Category


class NewsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = News
        fields = ["id", "text", "created_at", "main_category", "owner"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "news"]
