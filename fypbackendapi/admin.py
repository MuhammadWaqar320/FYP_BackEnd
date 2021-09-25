# username:waqar and password: 1234
# username:zahid and password: 1234
from django.contrib import admin
from .models import Product,Category,SubCategory
# Register your models here.
@admin.register(Product,Category,SubCategory)
class AllModels(admin.ModelAdmin):
    pass

