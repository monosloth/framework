from . import AbstractFacade


class ResolveFacade(AbstractFacade):

    def __init__(self):
        super().__init__('resolve')

    def invoke(self, clazz):
        return app('container').resolve(clazz)
