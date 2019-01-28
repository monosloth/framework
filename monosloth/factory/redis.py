import redis


class RedisFactory:

    def get(self, instance):
        """Instantiate and set a redis connection.

        :param instance: The instance to mutate.

        :return: The given instance.

        """
        connection = redis.Redis(
            host=config('cache.host'),
            port=config('cache.port'),
            db=config('cache.db')
        )

        instance.set_connection(connection)

        return instance
