import mysql.connector
import config

class mysqlConnect:
    def __init__(self, host=None, port=None, user=None, password=None, database=None):
        self.host = host or config.localhost
        self.port = port or config.db_port
        self.user = user or config.db_user
        self.password = password or config.db_password
        self.database = database or config.mysql_db
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
        )

    def fetch_data(self):
        if not self.connection:
            raise ConnectionError("Database Connection Error")
        cursor = self.connection.cursor()

        cursor.execute(config.query)
        data1 = cursor.fetchall()

        cursor.execute(config.query2)
        data2 = cursor.fetchall()

        cursor.close()
        return data1,data2
    
    def closeConn(self):
        if self.connection:
            self.connection.close()
            self.connection = None