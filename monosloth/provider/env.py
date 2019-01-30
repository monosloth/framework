import os
import yaml

from . import AbstractProvider
from monosloth.singleton import Environment


class EnvironmentProvider(AbstractProvider):

    def __init__(self):
        self.path = '.env.yaml'

    def register(self):
        """Load local & global environment variables.
        """
        params = vars(os.environ)

        if os.path.exists(self.path):
            with open(self.path) as stream:
                conf = yaml.load(stream)

                for key, value in conf.items():
                    params[key] = value

        Environment().set_environment_params(params)
