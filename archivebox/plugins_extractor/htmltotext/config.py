__package__ = 'plugins_extractor.htmltotext'


from abbx.archivebox.base_configset import BaseConfigSet


class HtmltotextConfig(BaseConfigSet):
    SAVE_HTMLTOTEXT: bool = True


HTMLTOTEXT_CONFIG = HtmltotextConfig()
