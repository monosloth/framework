from . import AbstractProvider
from monosloth.singleton import Cache


class CacheProvider(AbstractProvider):

    def register(self):
        """Set cache strategy.
        """
        strategy = "cache.{}".format(env('CACHE_DRIVER'))

        Cache().set_strategy(resolve(strategy))
