from rest_framework import serializers
from .models import Category, Product
import typing


class CategorySerializer(serializers.ModelSerializer):
    sku = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Category
        fields = '__all__'

    def validate(self, attrs):
        sku = attrs.pop('sku', None)
        print(sku)
        return super().validate(attrs)


class CreateCategorySerializer(serializers.ModelSerializer):
    sku = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = ['name', 'description', 'sku']

    def validate(self, attrs):
        sku = attrs.pop('sku', None)
        print(sku)
        return super().validate(attrs)


class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        data['category'] = CategorySerializer(instance.category).data if instance.category else None
        return data



