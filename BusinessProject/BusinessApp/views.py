from django.http import HttpResponse
from django.shortcuts import render, redirect
from BusinessApp.forms import Form_brands, Form_categories, Form_products
from BusinessApp.models import Brands, Categories, Products

# Create your views here.

def home(request):
    return render(request, 'BusinessApp/home.html')

def form_brands(request):
    if request.method == 'POST':
        my_form = Form_brands(request.POST)
        
        if my_form.is_valid():
            info = my_form.cleaned_data
            brand = Brands(name=info['name'], description=info['description']) #,logo=info['logo'])
            brand.save()
            return redirect('../main/')
    else:
        my_form = Form_brands()
        
    return render(request, 'BusinessApp/form_brands.html', {"form": my_form})

def form_categories(request):
    if request.method == 'POST':
        my_form = Form_categories(request.POST)
        
        if my_form.is_valid():
            info = my_form.cleaned_data
            category = Categories(name=info['name'], description=info['description'])
            category.save()
            return redirect('../main/')
    else:
        my_form = Form_categories()
        
    return render(request, 'BusinessApp/form_categories.html', {"form": my_form})
   
def form_products(request):
    if request.method == 'POST':
        my_form = Form_products(request.POST)
        
        if my_form.is_valid():
            info = my_form.cleaned_data
            product = Products(name=info['name'], description=info['description'], brand=info['brand'], category=info['category'], bar_code=info['bar_code'], price=info['price'], stock=info['stock'], active=info['active'])
            product.save()
            return redirect('../main/')
    else:
        my_form = Form_products()
    return render(request, 'BusinessApp/form_products.html', {"form": my_form})

def show_products(request):        
    res = Products.objects.all()
    return render(request, 'BusinessApp/main.html', {"res": res})

def res_lookup_products(request):        
    if request.GET['product']:
        product = request.GET['product']
        res = Products.objects.filter(name__icontains=product)
        if res:
            return render(request, 'BusinessApp/res_lookup_products.html', {"res": res, "product": product})
        else:
            product = request.GET['product']
            res_not_founded = f'No existe el producto: {product}'
            return render(request, 'BusinessApp/res_lookup_products.html', {"res_not_founded": res_not_founded, "product": product})
    else:
        res_not_founded = f'Su búsqueda es vacía, por favor completar la consulta'
        return render(request, 'BusinessApp/res_lookup_products.html', {"res_not_founded": res_not_founded})