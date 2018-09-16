from celery import group
from django.apps import apps

from mongo_sync.const import ALLOWED_OBJECTS_MAP
from taturana.celery import app


@app.task
def sync_task(object, hash):
    model = apps.get_model(*ALLOWED_OBJECTS_MAP[object].split('.'))
    result = model.sync_from_mongo(hash)
    return result


@app.task
def sync_all_movies():
    from movies.models import MongoFilm
    g = group(
        sync_task.s('film', f._id) for f in MongoFilm.objects.all()
    )
    return g()
