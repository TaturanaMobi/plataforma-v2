from taturana.celery import app
from mongo_sync.const import ALLOWED_OBJECTS_MAP
from django.apps import apps

@app.task
def sync_task(object, hash):
    model = apps.get_model(*ALLOWED_OBJECTS_MAP[object].split('.'))
    model.sync_from_mongo(hash)

