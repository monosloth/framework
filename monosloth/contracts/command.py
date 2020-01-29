from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):

    @abstractmethod
    def usage(self):
        """The command instruction."""
        pass

    @abstractmethod
    def run(self, input, output):
        """Invoke a command.

        :param input: An input interface.
        :param output: An output interface.

        """
        pass
