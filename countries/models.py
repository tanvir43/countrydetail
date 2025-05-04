from django.db import models


class Country(models.Model):
    # Model Schema for Country Information
    name = models.CharField(max_length=255)
    cca2 = models.CharField(max_length=2, unique=True)
    capital = models.CharField(max_length=255, null=True, blank=True)
    population = models.BigIntegerField()
    region = models.CharField(max_length=100, null=True, blank=True)
    timezones = models.JSONField(default=list)
    languages = models.JSONField(default=dict)
    flag_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
