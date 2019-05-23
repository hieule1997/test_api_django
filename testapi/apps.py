from django.apps import AppConfig


class TestapiConfig(AppConfig):
    name = 'testapi'

    def ready(self):
        # Makes sure all signal handlers are connected
        from . import handlers  # noqa
