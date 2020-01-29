from monosloth.contracts import Command

class BuildableCommand(Command):

    def set_usage(self, usage):
        """Set command usage.

        :param usage: The command instruction.

        """
        self.__usage = usage

    def set_strategy(self, strategy):
        """Set run strategy.
        
        :param strategy: The method to invoke on run.

        """
        self.__strategy = strategy

    def usage(self):
        """The command instruction."""
        return self.__usage

    def run(self, input, output):
        """Invoke a command.

        :param input: An input interface.
        :param output: An output interface.

        """
        self.__strategy(input, output)
