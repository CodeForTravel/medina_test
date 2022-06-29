from django.contrib import admin
from medina_test.apps.product import models as models_product

model_list = [
    models_product.WeatherType,
    models_product.ProductCategory,
    models_product.Product,
]

admin.site.register(model_list)