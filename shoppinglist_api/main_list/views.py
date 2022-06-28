from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ItemsSerializer
from .models import Items

class ItemsList(generics.ListCreateAPIView):
    queryset = Items.objects.all().order_by('id')
    serializer_class = ItemsSerializer

class ItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all().order_by('id')
    serializer_class = ItemsSerializer
