from django.db import models


class Country(models.Model):
    # Model Schema for Country Information
    name = models.CharField(max_length=100)
    official_name = models.CharField(max_length=200, blank=True, null=True)

    cca2 = models.CharField(max_length=2, unique=True)
    cca3 = models.CharField(max_length=3, unique=True)
    ccn3 = models.CharField(max_length=3, blank=True, null=True)
    cioc = models.CharField(max_length=3, blank=True, null=True)
    fifa = models.CharField(max_length=3, blank=True, null=True)

    capital = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    subregion = models.CharField(max_length=100, blank=True, null=True)
    continent = models.CharField(max_length=100, blank=True, null=True)

    area = models.FloatField(blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    independent = models.BooleanField(default=True)
    un_member = models.BooleanField(default=False)
    status = models.CharField(max_length=50, blank=True, null=True)

    start_of_week = models.CharField(max_length=20, blank=True, null=True)
    landlocked = models.BooleanField(default=False)

    latlng = models.JSONField(blank=True, null=True)
    capital_latlng = models.JSONField(blank=True, null=True)

    alt_spellings = models.JSONField(blank=True, null=True)
    tld = models.JSONField(blank=True, null=True)
    timezones = models.JSONField(blank=True, null=True)
    car_signs = models.JSONField(blank=True, null=True)
    car_side = models.CharField(max_length=10, blank=True, null=True)

    flag_emoji = models.CharField(max_length=10, blank=True, null=True)
    flag_url = models.URLField(blank=True, null=True)
    flag_svg = models.URLField(blank=True, null=True)
    coat_of_arms_png = models.URLField(blank=True, null=True)
    coat_of_arms_svg = models.URLField(blank=True, null=True)

    gini = models.JSONField(blank=True, null=True)
    postal_code = models.JSONField(blank=True, null=True)

    # Relations
    languages = models.ManyToManyField(Language, blank=True)
    currencies = models.ManyToManyField(Currency, blank=True)
    regional_blocs = models.ManyToManyField(RegionalBloc, blank=True)
    borders = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.name
