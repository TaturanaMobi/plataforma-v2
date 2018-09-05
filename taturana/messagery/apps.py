from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MessageryConfig(AppConfig):
    name = 'messagery'
    label = 'messagery'
    verbose_name = _("Messages and E-mails management")
