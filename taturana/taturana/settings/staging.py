from taturana.settings.base import *
DEBUG=False
EMAIL_HOST = 'mailhog'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

CELERY_RESULT_BACKEND = 'django-cache'

ALLOWED_HOSTS = ['127.0.0.1', 'admin.taturana']
