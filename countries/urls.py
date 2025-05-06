from django.urls import path
from countries import views as web_views

urlpatterns = [
    path('', web_views.CountryListView.as_view(), name='country-list'),
    path('countries/<int:pk>/', web_views.CountryDetailView.as_view(), name='country-detail'),
]