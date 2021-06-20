from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        """So that the signals can work.
        Django documentation recommends doing it this way to avoid some import side effects"""
        import users.signals