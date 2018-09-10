from celery.app import app_or_default

from messagery.models import Email
from movies.models import Film, Screening


app = app_or_default()

