from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=100)

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=200)
    description = serializers.CharField(required=True)
    price = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("the product name is too short")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("the price must be greater than 0")
        return value


class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=True)
    stars = serializers.IntegerField(required=True, min_value=1, max_value=5)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Review
        fields = '__all__'

    def validate_text(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("the review must be at least 10 characters long")
        return value
