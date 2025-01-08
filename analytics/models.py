from django.db import models

class Analytic(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    source = models.CharField(max_length=255)
    medium = models.CharField(max_length=255)
    campaign = models.CharField(max_length=255)
    ip = models.GenericIPAddressField()
    country = models.CharField(max_length=2)
    city = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source} - {self.medium}"
