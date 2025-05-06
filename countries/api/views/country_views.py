from django.db.models import Q

from rest_framework import generics
from countries.models import Country
from countries.api.serializers import CountrySerializer
from rest_framework.response import Response

from countries.api.views.base import AuthenticatedGenericAPIView


class CountryListCreateAPIView(AuthenticatedGenericAPIView, generics.ListCreateAPIView):
    """
    get:
    Return a list of all countries.

    post:
    Create a new country.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryRetrieveUpdateDestroyAPIView(AuthenticatedGenericAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return a single country.

    put:
    update a country.

    patch:
    partially update a country

    delete: 
    delete a country
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class SameRegionAPIView(AuthenticatedGenericAPIView, generics.ListAPIView):
    """
    get:
    Return same regional country list
    """
    serializer_class = CountrySerializer

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if not pk:
            return Response({"detail": "Country ID (pk) not provided."}, status=400)

        try:
            country = Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            return Response({"detail": "Country not found."}, status=404)

        queryset = Country.objects.filter(region=country.region).exclude(pk=country.pk).order_by('name')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CountrySearchAPIView(AuthenticatedGenericAPIView, generics.ListAPIView):
    """
    get:
    Return searched country
    """
    serializer_class = CountrySerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Country.objects.filter(name__icontains=query)
    



#For multi column based search
class MultiColCountrySearchAPIView(AuthenticatedGenericAPIView, generics.ListAPIView):
    """
    get:
    Search countries by name, capital, region, subregion, or cca2 (partial match).
    Example: /api/countries/search/?q=ca
    """
    serializer_class = CountrySerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '').strip()
        if not query:
            return Country.objects.none()

        return Country.objects.filter(
            Q(name__icontains=query) |
            Q(capital__icontains=query) |
            Q(region__icontains=query) |
            Q(subregion__icontains=query) |
            Q(cca2__icontains=query)
        )
