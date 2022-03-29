from decouple import config
import mariadb

class ConnectDB:

    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    # Connect to MariaDB Platform
    def make_connection(self):
        try:
            conn = mariadb.connect(
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port,
                database = self.database
                )
            return conn

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            #sys.exit(1)
        """
        finally:
            print("make_connection run.")
        """
