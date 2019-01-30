from . import AbstractProvider
from monosloth.singleton import Cache


class CacheProvider(AbstractProvider):

    def __init__(self, strategy):
        self.strategy = strategy

    def register(self):
        """Set cache strategy.
        """
        Cache().set_strategy(self.strategy)
