from . import AbstractFacade


class CallFacade(AbstractFacade):

    def __init__(self):
        super().__init__('call')

    def invoke(self):
        return resolve('singleton.command').call()
