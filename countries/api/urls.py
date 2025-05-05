from django.urls import path
from .views import (
    CountryListCreateAPIView,
    CountryRetrieveUpdateDestroyAPIView,
    SameRegionAPIView,
    CountriesByLanguageAPIView,
    CountrySearchAPIView,
)

urlpatterns = [
    path('countries/', CountryListCreateAPIView.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view(), name='country-detail'),
    path('countries/<int:pk>/same-region/', SameRegionAPIView.as_view(), name='same-region-countries'),
    path('languages/<str:code>/countries/', CountriesByLanguageAPIView.as_view(), name='countries-by-language'),
    path('countries/search/', CountrySearchAPIView.as_view(), name='country-search'),
]