"""backtur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from employees.api import EmployeeViewSet, OrganizationViewSet
from employees.views import employee_list, employee_detail, employee_by_organization
from clients.api import ClientViewSet, RussianPassportViewSet, InternationalPassportViewSet
from clients.views import clients_list, client_detail, rus_pas_by_client, rus_pas_detail
from preliminary_agreements.api import CountryViewSet, CityViewSet, PreliminaryAgreementViewSet, VisitingCityViewSet
from preliminary_agreements.views import agreements_list, agreement_detail, cities_by_country, visiting_cities_list, visiting_cities_by_agreement
from contracts.api import ContractViewSet, TripMemberViewSet, HotelViewSet, HotelReservationViewSet, RouteViewSet
from contracts.views import contracts_list, trip_members_by_contract, routes_by_agreement, add_trip_member, contract_detail, add_route, hotel_reservation_list


router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('organizations', OrganizationViewSet)

router.register('clients', ClientViewSet)
router.register('russian_passports', RussianPassportViewSet)
router.register('international_passports', InternationalPassportViewSet)

router.register('countries', CountryViewSet)
router.register('cities', CityViewSet)
router.register('preliminary_agreements', PreliminaryAgreementViewSet)
router.register('visiting_cities', VisitingCityViewSet)

router.register('contracts', ContractViewSet),
router.register('trip_members', TripMemberViewSet),
router.register('hotels', HotelViewSet),
router.register('hotel_reservations', HotelReservationViewSet),
router.register('routes', RouteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/employees/', employee_list),
    re_path(r'api/employees/(?P<pk>[0-9]+)$', employee_detail),
    path('api/clients/', clients_list),
    re_path(r'api/clients/(?P<pk>[0-9]+)$', client_detail),
    re_path(r'api/russian_passport$', rus_pas_by_client),
    re_path(r'api/russian_passport/(?P<pk>[0-9]+)$', rus_pas_detail),
    path('api/preliminary_agreements/', agreements_list),
    re_path(r'api/employees_by_org$', employee_by_organization),
    re_path(r'api/preliminary_agreements/(?P<pk>[0-9]+)$', agreement_detail),
    re_path(r'api/cities$', cities_by_country),
    path('api/cities/', visiting_cities_list),
    re_path(r'api/visiting_cities$', visiting_cities_by_agreement),
    path('api/contracts/', contracts_list),
    re_path(r'api/trip_members$', trip_members_by_contract),
    re_path(r'api/routes$', routes_by_agreement),
    path('api/add_trip_member/', add_trip_member),
    re_path(r'api/contracts/(?P<pk>[0-9]+)$', contract_detail),
    path('api/add_route/', add_route),
    path('api/hotel_reservation_list/', hotel_reservation_list),
]
