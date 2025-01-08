from django.urls import path
from .views import AnalyticCreateView, AnalyticListView, AnalyticStatsView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('create/', AnalyticCreateView.as_view(), name='create-analytic'),
    path('stats/', AnalyticStatsView.as_view(), name='stats-analytic'),
     path('list/', AnalyticListView.as_view(), name='list-analytic'),
]

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]