from django.urls import path
from BusinessApp.views import home, form_brands, form_categories, form_products, res_lookup_products, show_products

urlpatterns = [
    path('', home),
    path('main/', show_products),
    path('createBrands/', form_brands,  name="createBrands"),
    path('createCategories/', form_categories, name="createCategories"),    
    path('createProducts/', form_products, name="createProducts"),
    path('resLookupProducts/', res_lookup_products)
]