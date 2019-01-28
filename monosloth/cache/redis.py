from . import AbstractCache


class ArrayCache(AbstractCache):

    @abstractmethod
    def put(self, key, value):
        """Insert an item into the cache.

        :param key: The name of the value to insert.
        :param value: The value to insert.

        """
        self.get_connection().set(key, value)

    @abstractmethod
    def get(self, key):
        """Fetch a value from the cache.

        :param key: The name of the value to fetch.

        :return: The value associated with the given key.

        """
        self.get_connection().get(key)
