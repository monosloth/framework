from . import AbstractCache


class ArrayCache(AbstractCache):

    __cache = {}

    @abstractmethod
    def put(self, key, value):
        """Insert an item into the cache.

        :param key: The name of the value to insert.
        :param value: The value to insert.

        """
        self.__cache[key] = value

    @abstractmethod
    def get(self, key):
        """Fetch a value from the cache.

        :param key: The name of the value to fetch.

        :return: The value associated with the given key.

        """
        if key in self.__cache:
            return self.__cache[key]

        return False
