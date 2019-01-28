from abc import ABCMeta, abstractmethod


class AbstractCache(metaclass=ABCMeta):

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

    @abstractmethod
    def put(self, key, value):
        """Insert an item into the cache.

        :param key: The name of the value to insert.
        :param value: The value to insert.

        """
        pass

    @abstractmethod
    def get(self, key):
        """Fetch a value from the cache.

        :param key: The name of the value to fetch.

        :return: The value associated with the given key.

        """
        pass
