from django.shortcuts import render
from rest_framework import generics
from .models import Analytic
from .serializers import AnalyticSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class AnalyticCreateView(generics.CreateAPIView):
    queryset = Analytic.objects.all()
    serializer_class = AnalyticSerializer
    
class AnalyticStatsView(APIView):
    def get(self, request, *args, **kwargs):
        stats = Analytic.objects.values('campaign').annotate(count=Count('id')).order_by('-count')
        return Response(stats)

class AnalyticCreateView(generics.CreateAPIView):
    queryset = Analytic.objects.all()
    serializer_class = AnalyticSerializer

    def perform_create(self, serializer):
        ip = self.request.META.get('REMOTE_ADDR', '')
        country = self.request.META.get('GEO_COUNTRY', 'Unknown')
        city = self.request.META.get('GEO_CITY', 'Unknown')
        serializer.save(ip=ip, country=country, city=city)

class AnalyticListView(generics.ListAPIView):
    queryset = Analytic.objects.all()
    serializer_class = AnalyticSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['campaign', 'country', 'city']
    search_fields = ['source', 'medium']
    ordering_fields = ['created_at']
    ordering = ['-created_at']