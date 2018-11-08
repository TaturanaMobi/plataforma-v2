from django.contrib import admin

# Register your models here.
from .forms import EmailTemplateForm
from .models import Email, EmailTemplate

def email_name(obj):
    return obj.email.name
email_name.short_description = "E-mail"


class EmailTemplateInline(admin.TabularInline):
    model = EmailTemplate
    autocomplete_fields = ('film',)
    form = EmailTemplateForm


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = (email_name, 'film', 'active')
    autocomplete_fields = ('film',)


class EmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'active')
    inlines = [
        EmailTemplateInline
    ]


admin.site.register(Email, EmailAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)

