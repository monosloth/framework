from . import AbstractProvider
from monosloth.service.io import InputReader
from monosloth.service.io import OutputWriter

class CommandProvider(AbstractProvider):

    def __init__(self, *commands):
        self.commands = commands

    def register(self):

        for cmd in self.commands:
            resolve('singleton.command').register(cmd)
