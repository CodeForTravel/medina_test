from django.db import models


class WeatherType(models.Model):
    name = models.CharField(max_length=255)
    high_temp = models.IntegerField(default=40)
    low_temp = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    weather_type = models.ForeignKey(WeatherType, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title