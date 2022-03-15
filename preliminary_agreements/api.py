from rest_framework import viewsets
from rest_framework import permissions
from .models import Country, City, Preliminary_agreement, Visiting_city
from .serializers import CountrySerializer, CitySerializer, PreliminaryAgreementSerializer, VisitingCitySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.AllowAny]

class PreliminaryAgreementViewSet(viewsets.ModelViewSet):
    queryset = Preliminary_agreement.objects.all()
    serializer_class = PreliminaryAgreementSerializer
    permission_classes = [permissions.AllowAny]

class VisitingCityViewSet(viewsets.ModelViewSet):
    queryset = Visiting_city.objects.all()
    serializer_class = VisitingCitySerializer
    permission_classes = [permissions.AllowAny]