from django.urls import path
from .views import AnalyticCreateView, AnalyticStatsView

urlpatterns = [
    path('create/', AnalyticCreateView.as_view(), name='create-analytic'),
    path('stats/', AnalyticStatsView.as_view(), name='stats-analytic'),
     path('list/', AnalyticListView.as_view(), name='list-analytic'),
]