__package__ = 'archivebox.core'
__order__ = 100
import abx
import sys

# Provide a legacy top-level alias so imports like `import core.models`
# resolve to the same module object as `archivebox.core.models` and
# avoid registering models twice under different module names.
if 'core' not in sys.modules:
    sys.modules['core'] = sys.modules.get(__name__)

@abx.hookimpl
def register_admin(admin_site):
    """Register the core.models views (Snapshot, ArchiveResult, Tag, etc.) with the admin site"""
    from archivebox.core.admin import register_admin
    register_admin(admin_site)



@abx.hookimpl
def get_CONFIG():
    from archivebox.config.common import (
        SHELL_CONFIG,
        STORAGE_CONFIG,
        GENERAL_CONFIG,
        SERVER_CONFIG,
        ARCHIVING_CONFIG,
        SEARCH_BACKEND_CONFIG,
    )
    return {
        'SHELL_CONFIG': SHELL_CONFIG,
        'STORAGE_CONFIG': STORAGE_CONFIG,
        'GENERAL_CONFIG': GENERAL_CONFIG,
        'SERVER_CONFIG': SERVER_CONFIG,
        'ARCHIVING_CONFIG': ARCHIVING_CONFIG,
        'SEARCHBACKEND_CONFIG': SEARCH_BACKEND_CONFIG,
    }

