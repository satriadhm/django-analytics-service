from rest_framework import serializers
from .models import Analytic

class AnalyticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytic
        fields = '__all__'
