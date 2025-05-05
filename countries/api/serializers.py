from rest_framework import serializers
from ..models import Country, Language, Currency, RegionalBloc

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'code', 'name']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'code', 'name', 'symbol']

class RegionalBlocSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionalBloc
        fields = ['id', 'acronym', 'name']

class CountrySerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True, read_only=True)
    currencies = CurrencySerializer(many=True, read_only=True)
    regional_blocs = RegionalBlocSerializer(many=True, read_only=True)
    borders = serializers.SlugRelatedField(slug_field='cca3', many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'
