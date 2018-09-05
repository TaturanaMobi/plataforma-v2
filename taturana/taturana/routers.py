
class MongoRORouter:
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'movies':
            return 'mongo'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'auth':
            raise ValueError("Can't write to mongo!")
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'mongo' or \
           obj2._meta.app_label == 'mongo':
           return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'auth':
            return False
        return None
