import requests
from django.utils.deprecation import MiddlewareMixin

class GeoLocationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR', '')
        if ip:
            # Gunakan API geolokasi (contoh: ip-api.com)
            response = requests.get(f'http://ip-api.com/json/{ip}')
            if response.status_code == 200:
                data = response.json()
                request.META['GEO_COUNTRY'] = data.get('countryCode', 'Unknown')
                request.META['GEO_CITY'] = data.get('city', 'Unknown')
