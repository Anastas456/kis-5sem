from rest_framework import serializers
from .models import Country, City, Preliminary_agreement, Visiting_city

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class PreliminaryAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preliminary_agreement
        fields = '__all__'

class VisitingCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Visiting_city
        fields = '__all__'