from django.contrib import admin

# Register your models here.
from .models import MongoFilm

class FilmAdmin(admin.ModelAdmin):
    list_display = ('_id', 'title', 'status')

admin.site.register(MongoFilm, FilmAdmin)
