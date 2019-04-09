from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response

from backend.models import PlaceInfo
from backend.api import serializers


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 30

    def get_paginated_response(self, data):
        return Response({
            'page': self.page.number,
            'count': self.page_size,
            'total': self.page.paginator.count,
            'results': data
        })

    def get_page_size(self, request):
        if request.query_params.get(self.page_size_query_param) == 'max':
            self.max_page_size = 50000
            return self.max_page_size
        return super(LargeResultsSetPagination, self).get_page_size(request)


class PlaceListView(generics.ListAPIView):
    queryset = PlaceInfo.objects.get_queryset().order_by('id').only(
        'id',
        'name',
        'city',
        'area',
        'address',
        'guestRoomReferencePrice',
        'minMealCost',
    )
    serializer_class = serializers.PlaceListSerializer
    pagination_class = LargeResultsSetPagination


class PlaceDetailView(generics.RetrieveAPIView):

    queryset = PlaceInfo.objects.get_queryset()
    serializer_class = serializers.PlaceDetailSerializer

