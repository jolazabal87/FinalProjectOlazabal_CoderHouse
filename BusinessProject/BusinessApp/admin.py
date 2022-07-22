from django.contrib import admin
from .models import *

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    
class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Ticketet)
admin.site.register(Detail_ticket)
admin.site.register(Avatar)
admin.site.register(Blog)