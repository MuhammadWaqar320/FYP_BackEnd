from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Event, Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields='__all__'