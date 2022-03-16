from rest_framework import viewsets
from rest_framework import permissions
from .models import Contract, Trip_member, Hotel, Hotel_reservation, Route
from .serializers import ContractSerializer, TripMemberSerializer, HotelSerializer, HotelReservationSerializer, RouteSerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.AllowAny]

class TripMemberViewSet(viewsets.ModelViewSet):
    queryset = Trip_member.objects.all()
    serializer_class = TripMemberSerializer
    permission_classes = [permissions.AllowAny]

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.AllowAny]

class HotelReservationViewSet(viewsets.ModelViewSet):
    queryset = Hotel_reservation.objects.all()
    serializer_class = HotelReservationSerializer
    permission_classes = [permissions.AllowAny]

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.AllowAny]