
class MongoRORouter:
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """Send all read operations on Example app models to `example_db`."""
        if model._meta.model_name.startswith('mongo'):
            return 'mongo'
        return None

    def db_for_write(self, model, **hints):
        """Send all write operations on Example app models to `example_db`."""
        if model._meta.model_name.startswith('mongo'):
            return 'mongo'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Determine if relationship is allowed between two objects."""

        # Allow any relation between two models that are both in the Example app.
        if obj1._meta.model_name.startswith('mongo') or obj2._meta.model_name.startswith('mongo'):
            return False

        # Block relationship if one object is in the Example app and the other isn't.
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the Example app's models get created on the right database."""
        if model_name.startswith('mongo'):
            return False

        # No opinion for all other scenarios
        return None
