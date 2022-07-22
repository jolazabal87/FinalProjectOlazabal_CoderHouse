from django.urls import path
from TicketApp.views import add_movie, delete_movie, subtract_movie, clean_ticket

app_name = 'TicketApp'

urlpatterns = [
    path('add_movie/<int:movie_id>/', add_movie, name='add_movie'),
    path('delete_movie/<int:movie_id>/', delete_movie, name='delete_movie'),
    path('subtract_movie/<int:movie_id>/', subtract_movie, name='subtract_movie'),
    path('clean_ticket/', clean_ticket, name='clean_ticket'),
]

