from itertools import product
from django.contrib import admin
from .models import Client, Bill, Bill_Product, Product

# Register your models here.
admin.site.register(Client)
admin.site.register(Bill)
admin.site.register(Bill_Product)
admin.site.register(Product)

