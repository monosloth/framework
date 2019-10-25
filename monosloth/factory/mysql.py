import pymysql


class MySQLFactory:

    def get(self, instance):
        """Instantiate and set a mysql connection.

        :param instance: The instance to mutate.

        :return: The given instance.

        """
        connection = pymysql.connect(
            host=env('MYSQL_HOST'),
            user=env('MYSQL_USER'),
            password=env('MYSQL_PASSWORD'),
            db=env('MYSQL_DATABASE'),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

        instance.set_connection(connection)

        return instance
