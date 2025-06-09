__package__ = 'archivebox.api'

from django.apps import AppConfig

import abbx


class APIConfig(AppConfig):
    name = 'api'


@abbx.hookimpl
def register_admin(admin_site):
    from api.admin import register_admin
    register_admin(admin_site)
