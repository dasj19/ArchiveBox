__package__ = 'abbx.django'

from django.apps import AppConfig


class abbxConfig(AppConfig):
    name = 'abbx'

    def ready(self):
        import abbx
        from django.conf import settings
        
        abbx.pm.hook.ready(settings=settings)
