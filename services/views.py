#from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ServicesSerializador,PaymentUserSerializador, ExpiredPaymentsSerializador
from .models import Services, Payment_user, Expired_payments
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

@api_view(['GET'])
def services(request):
    print(request)
    
    if request.method == 'GET':
        servicios = Services.objects.all()
        pagination = PageNumberPagination()
        page = pagination.paginate_queryset(servicios,request)
        serializer = ServicesSerializador(page, many=True)
        return pagination.get_paginated_response(serializer.data)
    
    # if request.method == 'POST':
    #     print(request.data)
    #     serializer = ServicesSerializador(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status = status.HTTP_201_CREATED)
        
    #     return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST', 'PUT'])
def payment_user(request):
    print(request)
    filter_backends = [filters.SearchFilter]
    search_fields = ['paymentDate']
    if request.method == 'GET':
        paymentuser = Payment_user.objects.all()
        serializer = PaymentUserSerializador(paymentuser, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        print(request.data)
        serializer = PaymentUserSerializador(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def expired_payments(request):
    print(request)
    if request.method == 'GET':
        expired = Expired_payments.objects.all()
        serializer = ExpiredPaymentsSerializador(expired, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        print(request.data)
        serializer = ExpiredPaymentsSerializador(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)

def index(request):
    if request.method == 'GET':
        return HttpResponse('Index')
