from . database import AbstractDatabase


class MySQLDatabase(AbstractDatabase):

    def query(self, sql, params=()):
        """Invoke the given query & return a cursor.

        :param sql: The query to invoke.
        :param params: The query parameters.

        :return: A mysql cursor.

        """
        with self.connection.cursor() as cursor:
            return cursor.execute(sql, params)
