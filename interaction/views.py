from multiprocessing import context
from statistics import mode
from unittest import result
from django.shortcuts import render
from rest_framework.permissions import  IsAuthenticated, AllowAny
from rest_framework.filters import  SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework import generics, status, viewsets
from django.contrib.contenttypes.models import ContentType
from .serializers import RequestSerializer, RequestCreateSerializer, ReqeuestedSerializer
from data_v.serializers import HOPRMAXVoteSerializer, HOPRResultsSerializer, RCResultsSerializer, RcMAXVoteSerializer, RequestViewSerializer,\
    HOPRGeneralSerializer, RCGeneralSerializer
from .models import Request
from rest_framework import mixins
from api.authentication.backends import ActiveSessionAuthentication


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



@api_view(['POST', 'GET'])
@authentication_classes([ActiveSessionAuthentication,])
@permission_classes([IsAuthenticated])
def request_create(request, model):
    if request.method == 'POST':
        models = ContentType.objects.get(model=model)
        serializer = RequestCreateSerializer(data=request.data, context={'request', request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)

    if request.method == 'GET':
        models = ContentType.objects.get(model=model)
        data = models.model_class()
        
        if model == 'newvotehoprgeneral':
            inst = data.objects.all()
            serializer = HOPRGeneralSerializer(inst, many=True)
            return Response(serializer.data)
        if model == 'newvotehopresult':
            inst = data.objects.all()
            serializer = HOPRResultsSerializer(inst, many=True).prefetch_related('candidate')
            return Response(serializer.data)
        if model == 'newvotehoprmax':
            inst = data.objects.all().prefetch_related('result__candidate')
            serializer = RequestViewSerializer(inst, many=True)
            return Response(serializer.data)
        if model == 'newvotercgeneral':
            inst = data.objects.all().prefetch_related('result__candidate')
            serializer = RCGeneralSerializer(inst, many=True)
            return Response(serializer.data)
        if model == 'newvotercresult':
            inst = data.objects.all().prefetch_related('result__candidate')
            serializer = RCResultsSerializer(inst, many=True)
            return Response(serializer.data)
        if model == 'newvotercmax':
            inst = data.objects.all().prefetch_related('result__candidate')
            serializer = RcMAXVoteSerializer(inst, many=True)
            return Response(serializer.data)

   

