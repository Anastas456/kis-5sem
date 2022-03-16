from rest_framework import serializers
from .models import Contract, Trip_member, Hotel, Hotel_reservation, Route

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class TripMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip_member
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class HotelReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel_reservation
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'