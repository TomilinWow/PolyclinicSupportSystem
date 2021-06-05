import pymysql


class ConnectDb:

    def connect_db(self):
        """
        Установка связи с базой данных (self.connection)
        """
        try:
            self.connection = pymysql.connect(
                host="localhost",
                port=3306,
                user='root',
                password='user',
                database='hospital',
                cursorclass=pymysql.cursors.DictCursor
            )

        except Exception as ex:
            pass

        return self.connection