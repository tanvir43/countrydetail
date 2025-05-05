from rest_framework import generics
from countries.models import Country, Language
from countries.api.serializers import CountrySerializer

class CountriesByLanguageAPIView(generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        return Country.objects.filter(languages__code=self.kwargs['code'])