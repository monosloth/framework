from monosloth.builder import BuildableCommand


class register:
    """Command Decorator"""

    def __init__(self, name):
        """Decorator constructor.

        :param name: The command name.

        """
        self.name = name

    def __call__(self, f):
        """Register the command.

        :param f: The method to invoke.

        """
        cmd = BuildableCommand()
        cmd.set_usage(self.name)
        cmd.set_strategy(f)            

        resolve('singleton.command').register(cmd)
