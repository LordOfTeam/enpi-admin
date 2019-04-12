from django.db.models import Q
from django_filters import rest_framework as filters

from backend.models import PlaceInfo


class PlaceListFilter(filters.FilterSet):
    people_gte = filters.NumberFilter(field_name='ballrooms__maxPeople', lookup_expr='gte')
    people_lte = filters.NumberFilter(field_name='ballrooms__maxPeople', lookup_expr='lte')
    price_lte = filters.NumberFilter(field_name='ballrooms__allDayPrice', lookup_expr='lte')
    price_gte = filters.NumberFilter(field_name='ballrooms__allDayPrice', lookup_expr='gte')
    area_gte = filters.NumberFilter(field_name='ballrooms__area', lookup_expr='gte')
    area_lte = filters.NumberFilter(field_name='ballrooms__area', lookup_expr='lte')
    height_gte = filters.NumberFilter(field_name='ballrooms__height', lookup_expr='gte')

    class Meta:
        model = PlaceInfo
        fields = [
            'city',        # 城市： 默认：上海市
            'area',        # 行政区域，例如虹口区、浦东新区
            'people_gte',  # 大于等于人数
            'people_lte',  # 小于等于人数
            'price_lte',   # 小于等于价格
            'price_gte',   # 大于等于价格
            'area_gte',    # 大于等于面积
            'area_lte',    # 小于等于面积
            'height_gte'   # 大于等于层高
        ]
