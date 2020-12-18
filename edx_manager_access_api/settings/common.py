import os

def plugin_settings(settings):
    """
    Modify the provided settings object with settings specific to this plugin.
    """
    settings.AUTH_USERNAME = os.environ.get('AUTH_USERNAME')
    settings.AUTH_PASSWORD = os.environ.get('AUTH_PASSWORD')