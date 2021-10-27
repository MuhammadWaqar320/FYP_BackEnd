from django.db.models.query import QuerySet
from django.shortcuts import render
from .serializers import EventSerializer, ProductSerializer, ShipperSerializer
from .models import Event, Product,Shipper
from rest_framework import serializers, viewsets
# Create your views here.
class ProductView(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
class EventView(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
class ShipperView(viewsets.ModelViewSet):
    queryset=Shipper.objects.all()
    serializer_class=ShipperSerializer
    