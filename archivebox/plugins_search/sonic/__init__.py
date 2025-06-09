__package__ = 'plugins_search.sonic'
__label__ = 'sonic'
__version__ = '2024.10.14'
__author__ = 'ArchiveBox'
__homepage__ = 'https://github.com/valeriansaliou/sonic'
__dependencies__ = []

import abbx


@abbx.hookimpl
def get_PLUGIN():
    return {
        'sonic': {
            'PACKAGE': __package__,
            'LABEL': __label__,
            'VERSION': __version__,
            'AUTHOR': __author__,
            'HOMEPAGE': __homepage__,
            'DEPENDENCIES': __dependencies__,
        }
    }

@abbx.hookimpl
def get_CONFIG():
    from .config import SONIC_CONFIG
    
    return {
        'sonic': SONIC_CONFIG
    }


@abbx.hookimpl
def get_BINARIES():
    from .binaries import SONIC_BINARY
    
    return {
        'sonic': SONIC_BINARY
    }


@abbx.hookimpl
def get_SEARCHBACKENDS():
    from .searchbackend import SONIC_SEARCH_BACKEND
    
    return {
        'sonic': SONIC_SEARCH_BACKEND,
    }

@abbx.hookimpl
def ready():
    from .config import SONIC_CONFIG
    SONIC_CONFIG.validate()
