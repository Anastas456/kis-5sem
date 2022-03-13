from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import Client, Russian_passport
from .serializers import ClientSerializer, RussianPassportSerializer


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def clients_list(request):
    clients = Client.objects.all()

    if request.method == 'GET': 
        clients_serializer = ClientSerializer(clients, many=True)
        return JsonResponse(clients_serializer.data, safe=False)

    elif request.method == 'POST':
        client_data = JSONParser().parse(request)
        client_serializer = ClientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse(client_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])  
@permission_classes([AllowAny])
def client_detail(request, pk):
    client = Client.objects.get(pk=pk)

    if request.method == 'GET': 
        client_serializer = ClientSerializer(client) 
        return JsonResponse(client_serializer.data)

    elif request.method == 'PUT': 
        client_data = JSONParser().parse(request) 
        client_serializer = ClientSerializer(client, data=client_data) 
        if client_serializer.is_valid(): 
            client_serializer.save() 
            return JsonResponse(client_serializer.data) 
        return JsonResponse(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        try:
            client.delete() 
        except Exception as e:
            pass
            # print(e)
        return JsonResponse({'message': 'Client was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def rus_pas_by_client(request):
    # rus_passports = Russian_passport.objects.all()
    

    if request.method == 'GET': 
        try:
            rus_passports = Russian_passport.objects.all()
            client = request.GET.get('client', None)
            filtered_passports = rus_passports.filter(client__exact=client)
            passport_serializer = RussianPassportSerializer(filtered_passports, many=True)
            return JsonResponse(passport_serializer.data[0], safe=False)
        except IndexError:
            return JsonResponse({'client': client})

        

        

    elif request.method == 'POST':
        rus_passports = Russian_passport.objects.all()
        # client = request.GET.get('client', None)
        # filtered_passport = rus_passports.filter(client__exact=client)
        # if not filtered_passport:
        pass_data = JSONParser().parse(request)
        pass_serializer = RussianPassportSerializer(data=pass_data)
        if pass_serializer.is_valid():
            pass_serializer.save()
            # print(client, filtered_passport)
            return JsonResponse(pass_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(pass_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     return JsonResponse({'message': 'This client already has a russian passport'}, status=status.HTTP_200_OK) 



@api_view(['GET', 'PUT'])  
@permission_classes([AllowAny])
def rus_pas_detail(request, pk):
    # rus_passport = Russian_passport.objects.get(pk=pk)

    if request.method == 'GET': 
        try:
            rus_passport = Russian_passport.objects.get(pk=pk)
            # passport_serializer = RussianPassportSerializer(rus_passport)
            # return JsonResponse(passport_serializer.data)
        except Russian_passport.DoesNotExist:
            return JsonResponse({"id": pk})

        passport_serializer = RussianPassportSerializer(rus_passport)
        return JsonResponse(passport_serializer.data)

    elif request.method == 'PUT': 
        rus_passport = Russian_passport.objects.get(pk=pk)
        passport_data = JSONParser().parse(request) 
        passport_serializer = RussianPassportSerializer(rus_passport, data=passport_data) 
        if passport_serializer.is_valid(): 
            passport_serializer.save() 
            return JsonResponse(passport_serializer.data) 
        return JsonResponse(passport_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


