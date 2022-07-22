from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Sum, FloatField

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Genero: {self.name}"
class Movie(models.Model):
    title = models.CharField(max_length=20)
    sinopsis = models.CharField(max_length=500)
    genre_name = models.ForeignKey(Genre, on_delete=models.CASCADE)
    mark = models.IntegerField()
    price = models.FloatField() 
    stock = models.IntegerField() 
    img = models.ImageField(upload_to='images', null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Película: {self.title}; img: {self.img}"
class Ticketet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def total(self):
        return self.Detail_ticket_set.aggregate(
            total = Sum(F("price") * F("quantity"), output_field = FloatField()) 
        )["total"]
class Detail_ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticketet, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Blog(models.Model):
    date_released = models.DateField()
    post = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='blog', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='avatars', null=True, blank=True)
    