# username:waqar and password: 1234
# username:zahid and password: 1234
from django.contrib import admin
from .models import Product,Category,SubCategory,Event,Shipper,Customer,SubmittedReview
# Register your models here.
@admin.register(Product,Category,SubCategory,Shipper,Event,Customer,SubmittedReview)
class AllModels(admin.ModelAdmin):
    admin.site.index_title="PakElectronics Admin Panel"
    admin.site.site_header="Well Come To PaKElectronics"
    

