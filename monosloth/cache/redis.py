from . import AbstractCache


class RedisCache(AbstractCache):

    def put(self, key, value):
        """Insert an item into the cache.

        :param key: The name of the value to insert.
        :param value: The value to insert.

        """
        self.get_connection().set(key, value)

    def get(self, key):
        """Fetch a value from the cache.

        :param key: The name of the value to fetch.

        :return: The value associated with the given key.

        """
        return self.get_connection().get(key)
