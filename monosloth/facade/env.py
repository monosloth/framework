from monosloth.singleton import Environment
from . import AbstractFacade


class EnvironmentFacade(AbstractFacade):

    def __init__(self):
        super().__init__('env')

    def invoke(self, attr):
        return Environment().get(attr)
