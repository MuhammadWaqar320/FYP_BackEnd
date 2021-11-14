from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Category, Customer, Event, Product,Shipper, SubCategory, SubmittedReview
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        depth=1
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields='__all__'
class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shipper
        fields='__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'
        depth=1
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory
        fields='__all__'
        depth=1
class SubmittedReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubmittedReview
        fields='__all__'
        depth=1