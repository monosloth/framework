from monosloth.singleton import MetaSingleton


class Command(metaclass=MetaSingleton):

    def __init__(self):
        self.__commands = {}

    def set_streams(self, input, output):
        self.__input = input
        self.__output = output

    def register(self, command):
        """Register a command.

        :param command: The command to register.

        """
        self.__commands[command.usage()] = command

    def dispatch(self, command):
        """Invoke a command with the given arguments.

        :param command: The command to invoke.

        """
        self.__commands[command.usage()].run(
            self.__input, 
            self.__output
        )

    def call(self):
        """Call command from args.

        Invoke the command provided by the command line arguments.

        """
        action = self.__input.action()

        if action not in self.__commands:
            self.__output.error('Command does not exist!')
            return

        self.dispatch(self.__commands[action])

