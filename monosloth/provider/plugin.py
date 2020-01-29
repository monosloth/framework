import builtins
import importlib

from . import AbstractProvider


class PluginProvider(AbstractProvider):

    def __init__(self, *plugins):
        self.plugins = plugins

    def register(self):
        for plugin in self.plugins:
            plugin.install()
