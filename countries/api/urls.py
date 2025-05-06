from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView as AccessTokenView,
    TokenRefreshView as RefreshTokenView,
)

from .views import (
    CountryListCreateAPIView,
    CountryRetrieveUpdateDestroyAPIView,
    SameRegionAPIView,
    CountriesByLanguageAPIView,
    CountrySearchAPIView,
)


urlpatterns = [
    path('token/', AccessTokenView.as_view(), name='access_token'),
    path('token/refresh/', RefreshTokenView.as_view(), name='refresh_token'),

    path('countries/', CountryListCreateAPIView.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view(), name='country-detail'),
    path('countries/<int:pk>/same-region/', SameRegionAPIView.as_view(), name='same-region-countries'),
    path('languages/<str:code>/countries/', CountriesByLanguageAPIView.as_view(), name='countries-by-language'),
    path('countries/search/', CountrySearchAPIView.as_view(), name='country-search'),   
]