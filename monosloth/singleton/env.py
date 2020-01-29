from monosloth.singleton import MetaSingleton


class Environment(metaclass=MetaSingleton):

    __params = {}

    def set_environment_params(self, params):
        """Set the environment parameters.

        :param params: The environment params to set.

        """
        self.params = params

    def get(self, key):
        """Get an environment value with the given key.

        :param key: The environment variable key.

        :return: The environment variable value.

        """
        if key in self.__params:
            return self.__params[key]

        return False
