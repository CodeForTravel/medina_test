from rest_framework import  serializers
from medina_test.apps.product import models as models_product


class WeatherTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_product.WeatherType
        fields = ['id', 'high_temp', "low_temp", "name"]


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models_product.ProductCategory
        fields = ['id', 'name', "description"]



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_product.Product
        fields = ["id", 'category', 'weather_type', "title", 'description', "quantity"]




        
