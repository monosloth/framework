from abc import ABCMeta, abstractmethod


class Plugin(metaclass=ABCMeta):

    @abstractmethod
    def install(self):
        pass
