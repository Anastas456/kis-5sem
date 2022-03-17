from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from .models import Currency, Payment
from .serializers import CurrencySerializer, PaymentSerializer
from contracts.models import Contract
from contracts.serializers import ContractSerializer



@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def payments_list(request):
    payments = Payment.objects.all()

    if request.method == 'GET': 
        payments_serializer = PaymentSerializer(payments, many=True)
        return JsonResponse(payments_serializer.data, safe=False)

    elif request.method == 'POST':
        payment_data = JSONParser().parse(request)
        payment_serializer = PaymentSerializer(data=payment_data)
        if payment_serializer.is_valid():
            payment_serializer.save()
            return JsonResponse(payment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def contracts_by_organization(request):
     
    if request.method == 'GET': 
        contracts = Contract.objects.all()
        organization = request.GET.get('organization', None)
        filtered_contracts = contracts.filter(organization__exact=organization)
        contract_serializer = ContractSerializer(filtered_contracts, many=True)
        return JsonResponse(contract_serializer.data, safe=False)
