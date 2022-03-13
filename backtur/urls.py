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
from employees.views import employee_list, employee_detail
from clients.api import ClientViewSet, RussianPassportViewSet, InternationalPassportViewSet
from clients.views import clients_list, client_detail, rus_pas_by_client, rus_pas_detail


router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('organizations', OrganizationViewSet)

router.register('clients', ClientViewSet)
router.register('russian_passports', RussianPassportViewSet)
router.register('international_passports', InternationalPassportViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/employees/', employee_list),
    re_path(r'api/employees/(?P<pk>[0-9]+)$', employee_detail),
    path('api/clients/', clients_list),
    re_path(r'api/clients/(?P<pk>[0-9]+)$', client_detail),
    re_path(r'api/russian_passport$', rus_pas_by_client),
    re_path(r'api/russian_passport/(?P<pk>[0-9]+)$', rus_pas_detail)
]
