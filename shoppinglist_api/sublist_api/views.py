from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import SublistSerializer
from .models import Sublist

class SublistList(generics.ListCreateAPIView):
    queryset = Sublist.objects.all().order_by('id')
    serializer_class = SublistSerializer

class SublistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sublist.objects.all().order_by('id')
    serializer_class = SublistSerializer
