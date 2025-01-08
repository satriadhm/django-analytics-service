from django.contrib import admin
from .models import Analytic

class AnalyticAdmin(admin.ModelAdmin):
    list_display = ('source', 'medium', 'campaign', 'ip', 'country', 'city', 'created_at')
    list_filter = ('campaign', 'country', 'city')
    search_fields = ('source', 'medium', 'campaign')

admin.site.register(Analytic, AnalyticAdmin)