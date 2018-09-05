from django.contrib import admin

# Register your models here.
from .models import Email, EmailTemplate

class  EmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'default_title')

admin.site.register(Email, EmailAdmin)
admin.site.register(EmailTemplate)

