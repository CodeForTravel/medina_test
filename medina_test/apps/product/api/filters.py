
from rest_framework import filters

class ProductFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filter_dict = {}

        weather_type = request.query_params.get("weather_type")
        category = request.query_params.get("category")

        if category:
            filter_dict["category"] = category

        if weather_type:
            filter_dict["weather_type"] = weather_type

        if filter_dict:
            queryset = queryset.filter(**filter_dict)

        return queryset
