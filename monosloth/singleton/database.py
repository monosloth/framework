from monosloth.singleton import MetaSingleton


class Database(metaclass=MetaSingleton):

    def set_strategy(self, strategy):
        """Set the database strategy.

        :param strategy: The strategy to use.

        """
        self.strategy = strategy
