from django.contrib import admin
from .models import Country, City, Preliminary_agreement, Visiting_city


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_name')
    list_filter = ('id', 'country_name')
    search_fields = ('id', 'country_name')


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'city_name')
    list_filter = ('id', 'country')
    search_fields = ('country', 'city_name')

class PreliminaryAgreementAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_agreement', 'organization', 'employee', 'country_of_visit', 'client', 'number_of_trip_members', 'start_date_of_trip', 'end_date_of_trip')
    list_filter = ('organization', 'country_of_visit', 'client')
    search_fields = ('organization', 'country_of_visit', 'client')

class VisitingCityAdmin(admin.ModelAdmin):
    list_display = ('id', 'preliminary_agreement', 'city')
    list_filter = ('id', 'preliminary_agreement', 'city')
    search_fields = ('id', 'preliminary_agreement', 'city')

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Preliminary_agreement, PreliminaryAgreementAdmin)
admin.site.register(Visiting_city, VisitingCityAdmin)