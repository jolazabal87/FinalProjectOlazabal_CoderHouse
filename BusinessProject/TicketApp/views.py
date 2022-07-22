from django.shortcuts import render, redirect
from TicketApp.ticket import Ticket
from BusinessApp.models import Movie, Avatar

# Create your views here.

def add_movie(request, movie_id):
    ticket = Ticket(request)
    movie = Movie.objects.get(id=movie_id)
    
    ticket.add_ticket(movie=movie)
    
    return redirect('show_movies_to_ticket')

def delete_movie(request, movie_id):
    ticket = Ticket(request)
    movie = Movie.objects.get(id=movie_id)
    
    ticket.delete_ticket(movie=movie)
    
    return redirect('show_movies_to_ticket')

def subtract_movie(request, movie_id):
    ticket = Ticket(request)
    movie = Movie.objects.get(id=movie_id)
    
    ticket.subtract_ticket(movie=movie)
    
    return redirect('show_movies_to_ticket')

def clean_ticket(request):
    ticket = Ticket(request)
    
    ticket.clean_ticket()

    return redirect('show_movies_to_ticket')

def buscar_url_avatar(user):
    avatar = Avatar.objects.filter(user=user)
    if avatar:
        return avatar[0].img.url
    return None
