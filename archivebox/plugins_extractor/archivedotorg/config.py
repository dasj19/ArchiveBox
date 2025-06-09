__package__ = 'plugins_extractor.archivedotorg'


from abbx.archivebox.base_configset import BaseConfigSet


class ArchivedotorgConfig(BaseConfigSet):
    SAVE_ARCHIVE_DOT_ORG: bool = True


ARCHIVEDOTORG_CONFIG = ArchivedotorgConfig()
