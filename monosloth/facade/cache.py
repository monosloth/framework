from monosloth.singleton import Cache

from . import AbstractFacade


class CacheFacade(AbstractFacade):

    def __init__(self):
        super().__init__('cache')

    def invoke(self, key=False, value=False):
        if key:
            if value:
                return Cache().put(key, value)
            return Cache().get(key)
        return Cache()
