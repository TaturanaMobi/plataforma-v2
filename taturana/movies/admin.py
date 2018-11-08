from django.contrib import admin

# Register your models here.
from .models import Film, Screening

class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    search_fields = ('title',)


class ScreeningAdmin(admin.ModelAdmin):
    list_display = ('film', 'date')
    search_fields = ('film',)


admin.site.register(Film, FilmAdmin)
admin.site.register(Screening, ScreeningAdmin)
