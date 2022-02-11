from unittest import result
from django.shortcuts import render
from rest_framework.permissions import  IsAuthenticated, AllowAny
from rest_framework.filters import  SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import RequestSerializer
from .models import Request

class RequstViewSetNot(generics.ListAPIView):
    queryset = Request.objects.filter(status=False)
    serializer_class = RequestSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
   


class RequstViewSetYes(generics.ListAPIView):
    queryset = Request.objects.filter(status=True)
    serializer_class = RequestSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
   

