from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Brands)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Clients)
admin.site.register(Suppliers)
admin.site.register(Purchase_order)