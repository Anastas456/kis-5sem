from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from requests import get
from bs4 import BeautifulSoup as bs

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


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def currency_list(request):
    
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Host":"www.cbr.ru:443",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
    }

    body = get('http://www.cbr.ru/currency_base/daily/', headers=headers)
    for_bs = body.text
    soup = bs(for_bs, 'html.parser')

    currency_list = Currency.objects.all()
    currency = soup.find_all('td')

    if request.method == 'POST':
        i = 4
        for item in currency_list:
            Currency.objects.filter(code=item.code).update(rate=float(currency[i].text.replace(',', '.')))
            i += 5

    # context = {
    #     'currency_list': currency_list

    # }
    # return render(request, 'documents/currency_list.html', context)

    currency_serializer = CurrencySerializer(currency_list, many=True)
    return JsonResponse(currency_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_last_currency(request):
    currency = Currency.objects.all()

    if request.method == 'GET': 
        currency_serializer = CurrencySerializer(currency, many=True)
        return JsonResponse(currency_serializer.data, safe=False)
