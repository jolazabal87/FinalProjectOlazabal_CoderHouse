from django import forms

class Form_brands(forms.Form):
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=50)
    #logo = forms.ImageField()

class Form_categories(forms.Form):
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=50)

class Form_products(forms.Form):
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=50)
    brand = forms.CharField(max_length=50)
    category = forms.CharField(max_length=20)
    bar_code = forms.IntegerField()
    price = forms.FloatField()
    stock = forms.IntegerField() 
    #img = forms.ImageField(upload_to='images/', null=True, blank=True)
    active = forms.BooleanField()
