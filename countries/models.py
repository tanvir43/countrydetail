from django.db import models


class Country(models.Model):
    # Model Schema for Country Information
    name_common = models.CharField(max_length=255)
    name_official = models.CharField(max_length=255, blank=True)
    
    cca2 = models.CharField(max_length=2, blank=True)
    cca3 = models.CharField(max_length=3, blank=True)
    ccn3 = models.CharField(max_length=3, blank=True)
    cioc = models.CharField(max_length=3, blank=True)

    independent = models.BooleanField(null=True)
    status = models.CharField(max_length=100, blank=True)
    un_member = models.BooleanField(null=True)

    capital = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=100, blank=True)
    subregion = models.CharField(max_length=100, blank=True)

    area = models.FloatField(null=True, blank=True)
    population = models.BigIntegerField(null=True, blank=True)
    
    flag_emoji = models.CharField(max_length=10, blank=True)
    flag_url = models.URLField(blank=True)
    
    languages = models.JSONField(blank=True, null=True)
    currencies = models.JSONField(blank=True, null=True)
    
    latlng = models.JSONField(blank=True, null=True)
    landlocked = models.BooleanField(null=True)
    
    demonyms = models.JSONField(blank=True, null=True)
    timezones = models.JSONField(blank=True, null=True)
    continents = models.JSONField(blank=True, null=True)
    maps = models.JSONField(blank=True, null=True)
    
    gini = models.JSONField(blank=True, null=True)
    borders = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name
