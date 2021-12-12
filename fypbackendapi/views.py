from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
from .serializers import CategorySerializer, CustomerSerializer, SpecialOfferSerializer, ProductSerializer, ContactUsSerializer,ShipperSerializer, SubCategorySerializer, SubmittedReviewSerializer
from .models import Category, SpecialOffer, Product, Shipper, SubCategory,Customer,SubmittedReview,ContactUs
from rest_framework import serializers, viewsets
# Create your views here.
class ProductView(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
class SpecialOfferView(viewsets.ModelViewSet):
    queryset=SpecialOffer.objects.all()
    serializer_class=SpecialOfferSerializer
class ShipperView(viewsets.ModelViewSet):
    queryset=Shipper.objects.all()
    serializer_class=ShipperSerializer
class CategoryView(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
class SubCategoryView(viewsets.ModelViewSet):
    queryset=SubCategory.objects.all()
    serializer_class=SubCategorySerializer
class CustomerView(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
class SubmittedReviewView(viewsets.ModelViewSet):
    queryset=SubmittedReview.objects.all()
    serializer_class=SubmittedReviewSerializer
class ContactUsView(viewsets.ModelViewSet):
    queryset=ContactUs.objects.all()
    serializer_class=ContactUsSerializer
    