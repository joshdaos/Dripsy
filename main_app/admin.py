from django.contrib import admin
from .models import SellerProfile, SellersFollowed, Product
# Register your models here.

admin.site.register(SellerProfile)
admin.site.register(SellersFollowed)
admin.site.register(Product)