from monosloth.singleton import MetaSingleton


class Cache(metaclass=MetaSingleton):

    def set_strategy(self, strategy):
        """Set the cache strategy.

        :param strategy: The strategy to use.

        """
        self.strategy = strategy

    def put(self, key, value):
        """Insert a value into the cache.

        :param key: The name of the value to insert.
        :param value: The value to insert.

        """
        self.strategy.put(key, value)

    def get(self, key):
        """Fetch a value from the cache.

        :param key: The name of the value to fetch.

        :return: The value associated with the given key.

        """
        return self.strategy.get(key)
