import os
import yaml

from . import AbstractProvider
from monosloth.singleton import Environment


class EnvironmentProvider(AbstractProvider):

    def __init__(self):
        self.path = './config/.env.yaml'

    def register(self):
        """Load local & global environment variables.
        """
        params = os.environ

        if os.path.exists(self.path):
            with open(self.path) as stream:
                params += yaml.load(stream)

        Environment().set_environment_params(params)
