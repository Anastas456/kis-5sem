from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from .models import Contract, Trip_member, Route, Hotel_reservation
from.serializers import ContractSerializer, TripMemberSerializer, RouteSerializer, HotelReservationSerializer





@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def contracts_list(request):
    contracts = Contract.objects.all()

    if request.method == 'GET': 
        contracts_serializer = ContractSerializer(contracts, many=True)
        return JsonResponse(contracts_serializer.data, safe=False)

    elif request.method == 'POST':
        contract_data = JSONParser().parse(request)
        contract_serializer = ContractSerializer(data=contract_data)
        if contract_serializer.is_valid():
            contract_serializer.save()
            return JsonResponse(contract_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(contract_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def trip_members_by_contract(request):
     
    if request.method == 'GET': 
        trip_members = Trip_member.objects.all()
        contract = request.GET.get('contract', None)
        filtered_members = trip_members.filter(contract__exact=contract)
        trip_members_serializer = TripMemberSerializer(filtered_members, many=True)
        return JsonResponse(trip_members_serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def routes_by_agreement(request):
     
    if request.method == 'GET': 
        routes = Route.objects.all()
        contract = request.GET.get('contract', None)
        filtered_routes = routes.filter(contract__exact=contract)
        routes_serializer = RouteSerializer(filtered_routes, many=True)
        return JsonResponse(routes_serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([AllowAny])
def add_trip_member(request):
    # trip_members = Trip_member.objects.all()

    if request.method == 'POST':
        member_data = JSONParser().parse(request)
        member_serializer = TripMemberSerializer(data=member_data)
        if member_serializer.is_valid():
            member_serializer.save()
            return JsonResponse(member_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])  
@permission_classes([AllowAny])
def contract_detail(request, pk):
    contract = Contract.objects.get(pk=pk)

    if request.method == 'GET': 
        contract_serializer = ContractSerializer(contract) 
        return JsonResponse(contract_serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def add_route(request):

    if request.method == 'POST':
        route_data = JSONParser().parse(request)
        route_serializer = RouteSerializer(data=route_data)
        if route_serializer.is_valid():
            route_serializer.save()
            return JsonResponse(route_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(route_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def hotel_reservation_list(request):
    reservations = Hotel_reservation.objects.all()

    if request.method == 'GET': 
        reservation_serializer = HotelReservationSerializer(reservations, many=True)
        return JsonResponse(reservation_serializer.data, safe=False)


