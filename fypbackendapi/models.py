from django.contrib.admin.decorators import register
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.deletion import CASCADE
# Create your models here.
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
    product_image=models.ImageField(upload_to='uploads/images',null=False,blank=False)
    product_brand=models.CharField(max_length=500)
    product_color=models.CharField(max_length=50)
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
  
