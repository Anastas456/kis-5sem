from django.contrib import admin
from .models import Contract, Trip_member, Hotel, Hotel_reservation, Route


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract_date', 'preliminary_agreement', 'organization', 'agent', 'client', 'start_date_of_trip', 'end_date_of_trip')
    list_filter = ('id', 'contract_date', 'preliminary_agreement', 'organization', 'client')
    search_fields = ('id', 'contract_date', 'preliminary_agreement', 'organization', 'client')

class TripMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract', 'client')
    list_filter = ('id', 'contract', 'client')
    search_fields = ('id', 'contract', 'client')

class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'hotel_name', 'address', 'number_of_stars')
    list_filter = ('id', 'city', 'number_of_stars')
    search_fields = ('id', 'city', 'hotel_name')

class HotelReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel', 'room_type', 'nutrition', 'start_date', 'end_date')
    list_filter = ('id', 'hotel')
    search_fields = ('id', 'hotel')

class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract', 'hotel_reservation')
    list_filter = ('id', 'contract', 'hotel_reservation')
    search_fields = ('id', 'contract', 'hotel_reservation')


admin.site.register(Contract, ContractAdmin)
admin.site.register(Trip_member, TripMemberAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Hotel_reservation, HotelReservationAdmin)
admin.site.register(Route, RouteAdmin)