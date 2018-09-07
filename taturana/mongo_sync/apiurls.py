from django.urls import path
from mongo_sync.views import Sync

app_name = 'mongo_sync'
urlpatterns = [
    path('sync/', Sync.as_view(), name='sync')
]
