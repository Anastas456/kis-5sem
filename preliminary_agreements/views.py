from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from .models import Country, City, Preliminary_agreement, Visiting_city
from .serializers import CountrySerializer, CitySerializer, PreliminaryAgreementSerializer, VisitingCitySerializer



@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def agreements_list(request):
    agreements = Preliminary_agreement.objects.all()

    if request.method == 'GET': 
        agreements_serializer = PreliminaryAgreementSerializer(agreements, many=True)
        return JsonResponse(agreements_serializer.data, safe=False)

    elif request.method == 'POST':
        agreement_data = JSONParser().parse(request)
        agreement_serializer = PreliminaryAgreementSerializer(data=agreement_data)
        if agreement_serializer.is_valid():
            agreement_serializer.save()
            return JsonResponse(agreement_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(agreement_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])  
@permission_classes([AllowAny])
def agreement_detail(request, pk):
    agreement = Preliminary_agreement.objects.get(pk=pk)

    if request.method == 'GET': 
        agreement_serializer = PreliminaryAgreementSerializer(agreement) 
        return JsonResponse(agreement_serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def cities_by_country(request):
    
    if request.method == 'GET': 
        cities = City.objects.all()
        country = request.GET.get('country', None)
        filtered_cities = cities.filter(country__exact=country)
        cities_serializer = CitySerializer(filtered_cities, many=True)
        return JsonResponse(cities_serializer.data, safe=False)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def visiting_cities_list(request):
    cities = Visiting_city.objects.all()

    if request.method == 'GET': 
        citiess_serializer = VisitingCitySerializer(cities, many=True)
        return JsonResponse(citiess_serializer.data, safe=False)

    elif request.method == 'POST':
        city_data = JSONParser().parse(request)
        city_serializer = VisitingCitySerializer(data=city_data)
        if city_serializer.is_valid():
            city_serializer.save()
            return JsonResponse(city_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(city_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def visiting_cities_by_agreement(request):
     
    if request.method == 'GET': 
        visiting_cities = Visiting_city.objects.all()
        agreement = request.GET.get('preliminary_agreement', None)
        filtered_cities = visiting_cities.filter(preliminary_agreement__exact=agreement)
        cities_serializer = VisitingCitySerializer(filtered_cities, many=True)
        return JsonResponse(cities_serializer.data, safe=False)

