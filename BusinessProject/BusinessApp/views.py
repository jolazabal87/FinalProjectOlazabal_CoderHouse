from django.shortcuts import render, redirect
from BusinessApp.forms import Form_contact, Form_genre, Form_movie, Form_register_user, Form_contact
from BusinessApp.models import Genre, Movie, Avatar, Blog, Ticketet, Detail_ticket
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import MovieSerializer
from TicketApp.ticket import Ticket
# Create your views here.

def home(request):
    return render(request, 'BusinessApp/home.html')

def main(request):    
    if request.user.is_authenticated:      
        return render(request, 'BusinessApp/main.html', {"url": buscar_url_avatar(request.user.id)})
    return render(request, 'BusinessApp/main.html')

def create_genre(request):
    if request.method == 'POST':
        my_form = Form_genre(request.POST)
        
        if my_form.is_valid():
            info = my_form.cleaned_data
            genre = Genre(name=info['name'], description=info['description']) 
            genre.save()
            return redirect('../main/')
    else:
        my_form = Form_genre()        
    return render(request, 'BusinessApp/form_genre.html', {"form": my_form, "url": buscar_url_avatar(request.user.id)})

def edit_genre(request, genre_name):
    genre = Genre.objects.get(name=genre_name)
    if request.method == 'POST':
        my_form = Form_genre(request.POST, request.FILES)
        if my_form.is_valid():
            info = my_form.cleaned_data
            genre.name=info['name']
            genre.description=info['description']
            genre.save()
            return redirect('../../main/')
    else:
        my_form = Form_genre(initial={'name':genre.name, "description":genre.description})
    return render(request, 'BusinessApp/edit_genre.html', {"form": my_form, "url": buscar_url_avatar(request.user.id)})

def delete_genre(request, genre_name):
    genre = Genre.objects.get(name=genre_name)
    genre.delete()
    return redirect('../../main/')
  
def create_movie(request):
    if request.method == 'POST':
        my_form = Form_movie(request.POST, request.FILES)
        
        if my_form.is_valid():
            info = my_form.cleaned_data
            movie = Movie(title=info['title'], sinopsis=info['sinopsis'], genre_name=info['genre_name'], mark=info['mark'], price=info['price'], stock=info['stock'], img=info['img'], active=info['active'])
            movie.save()
            return redirect('../main/')
    else:
        my_form = Form_movie()
    return render(request, 'BusinessApp/form_movie.html', {"form": my_form, "url": buscar_url_avatar(request.user.id)})

def edit_movie(request, movie_title):
    movie = Movie.objects.get(title=movie_title)
    if request.method == 'POST':
        my_form = Form_movie(request.POST, request.FILES)
        if my_form.is_valid():
            info = my_form.cleaned_data
            movie.title=info['title']
            movie.sinopsis=info['sinopsis']
            movie.genre_name=info['genre_name']
            movie.mark=info['mark']
            movie.price=info['price']
            movie.stock=info['stock']
            movie.img=info['img']
            movie.active=info['active']
            movie.save()
            return redirect('../../main/')
    else:
        my_form = Form_movie(initial={'title':movie.title, "sinopsis":movie.sinopsis, "genre_name":movie.genre_name, "mark":movie.mark, "price":movie.price, "stock":movie.stock, "img":movie.img, "active":movie.active})
    return render(request, 'BusinessApp/edit_movie.html', {"form": my_form, "url": buscar_url_avatar(request.user.id)})

def delete_movie(request, movie_title):
    movie = Movie.objects.get(title=movie_title)
    movie.delete()
    return redirect('../../main/')

def show_genres(request):        
    res = Genre.objects.all()
    return render(request, 'BusinessApp/genres.html', {"res": res, "url": buscar_url_avatar(request.user.id)})

def show_movies(request):        
    res = Movie.objects.all()
    return render(request, 'BusinessApp/movies.html', {"res": res, "url": buscar_url_avatar(request.user.id)})

def show_one_movie(request, movie_title):        
    res = Movie.objects.get(title=movie_title)
    return render(request, 'BusinessApp/one_movie.html', {"result": res, "url": buscar_url_avatar(request.user.id)})

def res_lookup_movies(request):        
    if request.GET['movie']:
        movie = request.GET['movie']
        res = Movie.objects.filter(title__icontains=movie)
        if res:
            return render(request, 'BusinessApp/res_lookup_movies.html', {"res": res, "movie": movie, "url": buscar_url_avatar(request.user.id)})
        else:
            movie = request.GET['movie']
            res_not_founded = f'No encontramos el título: {movie}'
            return render(request, 'BusinessApp/res_lookup_movies.html', {"res_not_founded": res_not_founded, "movie": movie, "url": buscar_url_avatar(request.user.id)})
    else:
        res_not_founded = f'Su búsqueda es vacía, por favor completar la consulta'
        return render(request, 'BusinessApp/res_lookup_movies.html', {"res_not_founded": res_not_founded, "url": buscar_url_avatar(request.user.id)})

def register_user(request):
    if request.method == 'POST':
        form = Form_register_user(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return redirect('../login/')
    else:
        form = Form_register_user()
    return render(request, 'BusinessApp/register_user.html', {"form": form, "msg": "REGISTER", "url": buscar_url_avatar(request.user.id)})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('../main/')
            else:
                return render(request, 'BusinessApp/login_user.html', {"msg": f"Error en los datos", "url": buscar_url_avatar(request.user.id)})
        else:
            return render(request, 'BusinessApp/login_user.html', {"msg": f"Formulario incorrecto", "url": buscar_url_avatar(request.user.id)})
    form = AuthenticationForm()
    return render(request, 'BusinessApp/login_user.html', {"form": form, "msg": "LOGIN", "url": buscar_url_avatar(request.user.id)})
      
def buscar_url_avatar(user):
    avatar = Avatar.objects.filter(user=user)
    if avatar:
        return avatar[0].img.url
    return None

def show_movies_to_ticket(request):        
    res = Movie.objects.all()
    return render(request, 'TicketApp/ticket.html', {"res": res, "url": buscar_url_avatar(request.user.id)})

def about_us(request):        
    return render(request, 'BusinessApp/about_us.html', {"url": buscar_url_avatar(request.user.id)})

def show_users(request):   
    users = User.objects.all()
    avatars = Avatar.objects.all()
    return render(request, 'BusinessApp/users.html', {"users": users, "avatars": avatars, "url": buscar_url_avatar(request.user.id)})

def contact(request):   
    my_form = Form_contact()
    if request.method == 'POST':
        my_form = Form_contact(data=request.POST)
        if my_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            text = request.POST.get('text')            
            return render(request, 'BusinessApp/contact_ok_msg.html', {"url": buscar_url_avatar(request.user.id)})

    return render(request, 'BusinessApp/contact.html', { "form": my_form, "url": buscar_url_avatar(request.user.id)})

def blog(request):   
    posts = Blog.objects.all()
    return render(request, 'BusinessApp/blog.html', {"posts":posts, "url": buscar_url_avatar(request.user.id)})

def ticket(request):
    ticketet = Ticketet.objects.create(user=request.user)
    ticket = Ticket(request)
    detail_ticket = list()
    for key, value in ticket.ticket.items():
        detail_ticket.append(Detail_ticket(
            movie_id=key,
            quantity=value["quantity"],
            user=request.user,
            ticket=ticketet
        )    
        )
    Detail_ticket.objects.bulk_create(detail_ticket)
    return render(request, 'TicketApp/ticket_ok_msg.html', {"url": buscar_url_avatar(request.user.id)})
class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
