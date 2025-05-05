from rest_framework import generics
from countries.models import Country
from countries.api.serializers import CountrySerializer
from rest_framework.response import Response

class CountryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class SameRegionAPIView(generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        country = Country.objects.get(pk=self.kwargs['pk'])
        return Country.objects.filter(region=country.region).exclude(pk=country.pk)


class CountrySearchAPIView(generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Country.objects.filter(name__icontains=query)