from . import AbstractProvider
from monosloth.singleton import Database


class DatabaseProvider(AbstractProvider):

    def register(self):
        """Set database strategy.
        """
        strategy = "database.{}".format(env('DATABASE_DRIVER'))

        Database().set_strategy(resolve(strategy))
