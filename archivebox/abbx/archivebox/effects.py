"""
Hookspec for side-effects that ArchiveBox plugins can trigger.

(e.g. network requests, binary execution, remote API calls, external library calls, etc.)
"""

__package__ = 'abbx.archivebox'

import abbx


@abbx.hookspec
def check_remote_seed_connection(urls, extractor, credentials, created_by):
    pass


@abbx.hookspec
def exec_extractor(url, extractor, credentials, config):
    pass

