import pymysql



class Connection:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.connection.cursor()

    def isConnected(self):
        if self.connection is None:
            print("Error in connection")
        else:
            print("Connected")
