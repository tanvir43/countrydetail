import json
import requests
from django.core.management.base import BaseCommand
from countries.models import Country, Currency, Language

class Command(BaseCommand):
    """
    Fetch and store country data from restcountries API 
    """
    help = 'Fetches country data from restcountries API and populates the database.'

    def handle(self, *args, **options):
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR("Failed to fetch data"))
            return

        data = response.json()
        self.stdout.write(f"Fetched {len(data)} countries.")

        for item in data:
            name = item.get("name", {})
            common_name = name.get("common")
            official_name = name.get("official")

            cca2 = item.get("cca2")
            cca3 = item.get("cca3")
            ccn3 = item.get("ccn3")
            cioc = item.get("cioc")
            fifa = item.get("fifa")

            region = item.get("region")
            subregion = item.get("subregion")
            continent = item.get("continents", [None])[0]

            capital = item.get("capital", [None])
            capital = capital[0] if capital else None

            latlng = item.get("latlng")
            capital_latlng = item.get("capitalInfo", {}).get("latlng")

            car = item.get("car", {})
            car_signs = car.get("signs")
            car_side = car.get("side")

            flags = item.get("flags", {})
            flag_emoji = item.get("flag")
            flag_url = flags.get("png")
            flag_svg = flags.get("svg")

            coat = item.get("coatOfArms", {})
            coat_png = coat.get("png")
            coat_svg = coat.get("svg")

            gini = item.get("gini")
            postal_code = item.get("postalCode")

            # country_obj, created = Country.objects.update_or_create(
            #     cca3=cca3,
            #     defaults={
            #         "name": common_name,
            #         "official_name": official_name,
            #         "cca2": cca2,
            #         "ccn3": ccn3,
            #         "cioc": cioc,
            #         "fifa": fifa,
            #         "capital": capital,
            #         "region": region,
            #         "subregion": subregion,
            #         "continent": continent,
            #         "area": item.get("area"),
            #         "population": item.get("population"),
            #         "independent": item.get("independent", True),
            #         "un_member": item.get("unMember", False),
            #         "status": item.get("status"),
            #         "start_of_week": item.get("startOfWeek"),
            #         "landlocked": item.get("landlocked", False),
            #         "latlng": latlng,
            #         "capital_latlng": capital_latlng,
            #         "alt_spellings": item.get("altSpellings"),
            #         "tld": item.get("tld"),
            #         "timezones": item.get("timezones"),
            #         "car_signs": car_signs,
            #         "car_side": car_side,
            #         "flag_emoji": flag_emoji,
            #         "flag_url": flag_url,
            #         "flag_svg": flag_svg,
            #         "coat_of_arms_png": coat_png,
            #         "coat_of_arms_svg": coat_svg,
            #         "gini": gini,
            #         "postal_code": postal_code,
            #     }
            # )

            if Country.objects.filter(cca3=cca3).exists():
                self.stdout.write(self.style.WARNING(f"Skipped (already exists): {common_name}"))
                continue

            country_obj = Country.objects.create(
                name=common_name,
                official_name=official_name,
                cca2=cca2,
                cca3=cca3,
                ccn3=ccn3,
                cioc=cioc,
                fifa=fifa,
                capital=capital,
                region=region,
                subregion=subregion,
                continent=continent,
                area=item.get("area"),
                population=item.get("population"),
                independent=item.get("independent", True),
                un_member=item.get("unMember", False),
                status=item.get("status"),
                start_of_week=item.get("startOfWeek"),
                landlocked=item.get("landlocked", False),
                latlng=latlng,
                capital_latlng=capital_latlng,
                alt_spellings=item.get("altSpellings"),
                tld=item.get("tld"),
                timezones=item.get("timezones"),
                car_signs=car_signs,
                car_side=car_side,
                flag_emoji=flag_emoji,
                flag_url=flag_url,
                flag_svg=flag_svg,
                coat_of_arms_png=coat_png,
                coat_of_arms_svg=coat_svg,
                gini=gini,
                postal_code=postal_code,
            )

            # Handle Languages
            country_obj.languages.clear()
            for code, lang_name in item.get("languages", {}).items():
                language_obj, _ = Language.objects.get_or_create(code=code, defaults={"name": lang_name})
                country_obj.languages.add(language_obj)

            # Handle Currencies
            country_obj.currencies.clear()
            for code, currency_info in item.get("currencies", {}).items():
                currency_obj, _ = Currency.objects.get_or_create(
                    code=code,
                    defaults={
                        "name": currency_info.get("name"),
                        "symbol": currency_info.get("symbol"),
                    },
                )
                country_obj.currencies.add(currency_obj)

            # Handle Borders
            country_obj.borders.clear()
            for border_cca3 in item.get("borders", []):
                try:
                    border_country = Country.objects.get(cca3=border_cca3)
                    country_obj.borders.add(border_country)
                except Country.DoesNotExist:
                    continue

            self.stdout.write(self.style.SUCCESS(f"Created: {common_name}"))
