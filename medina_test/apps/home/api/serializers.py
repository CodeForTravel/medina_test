from rest_framework import  serializers
from medina_test.apps.home import models as models_home


class WeatherTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_home.WeatherType
        fields = ['id', 'high_temp', "low_temp" "name"]


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models_home.ProductCategory
        fields = ['id', 'name', "description"]



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_home.Product
        fields = ["id", 'category', 'weather_type', "title", 'description', "quantity"]




        
