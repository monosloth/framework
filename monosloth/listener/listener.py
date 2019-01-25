from abc import ABCMeta, abstractmethod


class AbstractListener(metaclass=ABCMeta):

    @abstractmethod
    def invoke(self, event):
        pass
