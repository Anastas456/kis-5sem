from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def employee_list(request):
    employees = Employee.objects.all()

    if request.method == 'GET': 
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse(employees_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(employees_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])  
@permission_classes([AllowAny])
def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'GET': 
        employees_serializer = EmployeeSerializer(employee) 
        return JsonResponse(employees_serializer.data)

    elif request.method == 'PUT': 
        employee_data = JSONParser().parse(request) 
        employees_serializer = EmployeeSerializer(employee, data=employee_data) 
        if employees_serializer.is_valid(): 
            employees_serializer.save() 
            return JsonResponse(employees_serializer.data) 
        return JsonResponse(employees_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        try:
            employee.delete() 
        except Exception as e:
            pass
            # print(e)
        return JsonResponse({'message': 'Employee was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def employee_by_organization(request):
    
    if request.method == 'GET': 
        employees = Employee.objects.all()
        organization = request.GET.get('organization', None)
        filtered_employees = employees.filter(organization__exact=organization)
        employee_serializer = EmployeeSerializer(filtered_employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
