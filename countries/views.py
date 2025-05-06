
from django.views.generic import ListView, DetailView
from countries.models import Country
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from countries.models import Country

@method_decorator(login_required, name='dispatch')
class CountryListView(ListView):
    """
    GET: 
    Country List View
    """
    model = Country
    template_name = 'countries/country_list.html'
    paginate_by = 10
    ordering = ['name']

    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = Country.objects.all()
        if query:
            qs = qs.filter(name__icontains=query)
        return qs.order_by('name')
    
    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return self.render_partial(context, **response_kwargs)
        return super().render_to_response(context, **response_kwargs)

    def render_partial(self, context, **response_kwargs):
        html = render_to_string('countries/_country_table.html', context, request=self.request)
        return JsonResponse({'html': html})


@method_decorator(login_required, name='dispatch')
class CountryDetailView(DetailView):
    """
    GET:
    Country Detail View
    """
    model = Country
    template_name = 'countries/country_detail.html'
    context_object_name = 'country'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = self.object
        context['same_region_countries'] = Country.objects.filter(region=country.region).exclude(pk=country.pk)
        context['spoken_languages'] = country.languages.all()
        return context
