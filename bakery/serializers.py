from rest_framework import serializers
from .models import Category, Flavour

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'point_five', 'one', 'one_point_five', 'two', 'twe_point_five', 'three']


class FlavourSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Flavour
        fields = ['name', 'category']