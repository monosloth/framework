class add:
    """Command Decorator"""

    def __init__(self, name, description):
        """Decorator constructor.

        :param name: The command name.
        :param description: The command description.

        """
        self.keys = keys

    def __call__(self, f):
        """Instantiate & inject the given class into the contextual function.

        :param f: The method to invoke.

        """
        def w(*args, **kwargs):
            return f(*args, **kwargs)

        return w
