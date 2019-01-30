import redis

from monosloth.singleton import Environment


class RedisFactory:

    def get(self, instance):
        """Instantiate and set a redis connection.

        :param instance: The instance to mutate.

        :return: The given instance.

        """
        connection = redis.Redis(
            host=env('REDIS_HOST'),
            port=env('REDIS_PORT'),
            db=env('REDIS_DB'),
            charset="utf-8",
            decode_responses=True
        )

        instance.set_connection(connection)

        return instance
