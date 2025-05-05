from rest_framework import generics, filters, permissions
from ..models import Country, Language
from .serializers import CountrySerializer
from django.db.models import Q

class CountryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'official_name', 'cca2', 'cca3']

class CountryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

class SameRegionAPIView(generics.ListAPIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        country = Country.objects.get(pk=self.kwargs['pk'])
        return Country.objects.filter(region=country.region).exclude(pk=country.pk)

class CountriesByLanguageAPIView(generics.ListAPIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        language_code = self.kwargs['code']
        return Country.objects.filter(languages__code=language_code)

class CountrySearchAPIView(generics.ListAPIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Country.objects.filter(Q(name__icontains=query) | Q(official_name__icontains=query))
