from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Genre

class Form_genre(forms.Form):
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=50)
   

class Form_movie(forms.Form):
    title = forms.CharField(max_length=20)
    sinopsis = forms.CharField(max_length=50)
    genre_name = forms.ModelChoiceField(
        queryset=Genre.objects.all()
        .order_by('name')
    )
    mark = forms.IntegerField()
    price = forms.FloatField()
    stock = forms.IntegerField() 
    img = forms.ImageField()
    active = forms.BooleanField()
class Form_contact(forms.Form):
    name = forms.CharField(max_length=20, label="name")
    email = forms.EmailField(label="email")
    text = forms.CharField(widget=forms.Textarea, label="text")    
class Form_register_user(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirmar contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}
