import sys

class InputReader:

    def __init__(self, parser):
        """InputReader constructor.

        :param parser: A command line parser.

        """
        self.__parser = parser
        self.__action = None
        self.__arguments = []
        self.__options = []

    def read(self):
        """Parse the command line args."""
        if len(sys.argv) > 1:
            self.__arguments, self.__options = self.__parser.parse(sys.argv[1:])
            self.__action = sys.argv[1]

    def option(self, name, default=False):
        """Get an option from the input options.

        :param name: The name of the option.
        :param default: The default value to return.
        :return: The value derived fromof the given name.

        """
        if name in self.__options:
            return self.__options[name]
        return default

    def argument(self, name, default=False):
        """Get an argument from the input arguments.

        :param name: The name of the argument.
        :param default: The default value to return.
        :return: The value of the given name.

        """
        if name in self.__arguments:
            return self.__arguments[name]
        return default

    def action(self):
        """Get the command name.

        :return: A string containing the command name.

        """
        return self.__action
