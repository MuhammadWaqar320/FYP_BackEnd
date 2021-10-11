from django.shortcuts import render
from .serializers import EventSerializer, ProductSerializer
from .models import Event, Product
from rest_framework import serializers, viewsets
# Create your views here.
class ProductView(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
class EventView(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    