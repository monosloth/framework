from abc import ABCMeta, abstractmethod


class AbstractDatabase(metaclass=ABCMeta):

    def set_connection(self, connection):
        """Set the cache connection instance.

        :param connection: A connection instance.

        """
        self.connection = connection

    def get_connection(self):
        """Get the connection instance.

        :return: A connection instance.

        """
        return self.connection
