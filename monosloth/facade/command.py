from monosloth.singleton import Command

from . import AbstractFacade


class CommandFacade(AbstractFacade):

    def __init__(self):
        super().__init__('command')

    def invoke(self, command=False):
        bus = resolve('singleton.command')
        if command:
            return bus.dispatch(command)
        return bus
