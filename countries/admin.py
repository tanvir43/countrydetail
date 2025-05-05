from django.contrib import admin
from countries.models import Country, Currency, Language

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "cca3", "region", "subregion", "capital", "population")
    search_fields = ("name", "cca3", "capital", "region")
    list_filter = ("region", "subregion", "un_member", "independent")
    filter_horizontal = ("currencies", "languages")

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "symbol")
    search_fields = ("code", "name")

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")
