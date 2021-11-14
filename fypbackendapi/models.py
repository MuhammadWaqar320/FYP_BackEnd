from django.contrib.admin.decorators import register
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.deletion import CASCADE
# Create your models here.
class Person(models.Model):
    person_id=models.AutoField(primary_key=True)
    person_name=models.CharField(max_length=150)
    person_email=models.EmailField(max_length=230)
    person_address=models.CharField(max_length=200)
    person_registerDate=models.DateTimeField()
    def __str__(self):
        return self.person_name
class Category(models.Model):
    category_name=models.CharField(max_length=350)
    class Meta:
        verbose_name_plural='Categories'
    def __str__(self):
        return self.category_name
class SubCategory(models.Model):
    subCategory_name=models.CharField(max_length=500)
    category=models.ForeignKey(Category,on_delete=CASCADE,default=1)
    verbose_name_plural='SubCategories'
    def __str__(self):
        return self.subCategory_name
class Product(models.Model):
    product_name=models.CharField(max_length=500)
    product_price=models.FloatField()
    product_description=RichTextField()
    product_brand=models.CharField(max_length=500)
    product_color=models.CharField(max_length=50)
    product_image=models.ImageField(upload_to='uploads/images',null=False,blank=False)
    product_companyName=models.CharField(max_length=500)
    product_total_stock=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=CASCADE)
    subCategory=models.ForeignKey(SubCategory,on_delete=CASCADE,default=1)
    def __str__(self):
        return self.product_name
class Event(models.Model):
    event_name=models.CharField(max_length=150)
    event_Finish_Time=models.DateTimeField()
    def __str__(self):
        return self.event_name
class Shipper(models.Model):
    shipper_name=models.CharField(max_length=150)
    shipper_email=models.EmailField(max_length=100)
    shipper_image=models.ImageField(upload_to='uploads/images',null=False,blank=False)
    shipper_phone_no=models.CharField(max_length=20)
    shipper_address=models.CharField(max_length=200)
    shipper_Regiter_Date=models.DateField()
    shipper_verified=models.BooleanField()
    shipper_detail=RichTextField(null=True)
    def __str__(self):
        return self.shipper_name
class Customer(Person,models.Model):
    customer_phone=models.CharField(max_length=20)
    customer_password=models.CharField(max_length=30)
    customer_phone_image=models.ImageField(upload_to='uploads/images',null=False,blank=False)
class SubmittedReview(Customer,Product,models.Model):
    Product_Id=models.ForeignKey(Product,on_delete=CASCADE,default=1,related_name="pro_id")
    Customer_Id=models.ForeignKey(Customer,on_delete=CASCADE,default=1,related_name="cus_id")
    rating=models.FloatField()