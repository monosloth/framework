from . import AbstractFacade


class DispatchFacade(AbstractFacade):

    def __init__(self):
        super().__init__('dispatch')

    def invoke(self, command):
        return resolve('singleton.command').dispatch(command)
