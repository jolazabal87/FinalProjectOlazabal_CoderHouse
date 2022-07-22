from django.urls import path
from BusinessApp.views import home, main, about_us, contact, blog, create_genre, edit_genre, delete_genre, create_movie, edit_movie, delete_movie, res_lookup_movies, show_genres, show_movies, show_users, show_movies_to_ticket, show_one_movie, register_user, login_user, ticket
from django.contrib.auth.views import LogoutView

from rest_framework.routers import SimpleRouter
from BusinessApp.views import MovieViewSet

router = SimpleRouter()
router.register(r"main/api", MovieViewSet)

urlpatterns = router.urls


urlpatterns += [
    path('', home),
    path('main/', main, name="main"),
    path('main/about_us/', about_us, name="about_us"),
    path('main/contact/', contact, name="contact"),
    path('main/blog/', blog, name="blog"), 
    path('main/genres', show_genres),    
    path('main/movies', show_movies),
    path('main/show_users', show_users, name="show_users"),
    path('main/show_movies_to_ticket', show_movies_to_ticket, name="show_movies_to_ticket"),
    path('oneMovie/<movie_title>/', show_one_movie, name="show_one_movie"),
    path('createGenre/', create_genre,  name="createGenre"),
    path('editGenre/<genre_name>/', edit_genre, name="editGenre"),
    path('deleteGenre/<genre_name>/', delete_genre, name="deleteGenre"),
    path('createMovie/', create_movie, name="createMovie"),
    path('editMovie/<movie_title>/', edit_movie, name="editMovie"),
    path('deleteMovie/<movie_title>/', delete_movie, name="deleteMovie"),
    path('resLookupMovies/', res_lookup_movies),
    path('register/', register_user, name="register_user"),
    path('login/', login_user, name="login_user"),
    path('logout/', LogoutView.as_view(template_name='BusinessApp/logout_user.html'), name='logout_user'),
    path('ticketet/', ticket, name="ticketet"),
]

