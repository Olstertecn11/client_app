import pymysql

class Query:

    def __init__(self, host, user, db, pw):
        self.conn = pymysql.connect(host=host, user=user, database=db, password=pw) 
        self.manager = self.conn.cursor()

    def createDatabase(self):
        sql = "CREATE DATABASE client"
        if not self.exist():
            self.manager.execute(sql)
            print("La base de datos <client> ha sido creada")
        else:
            print("La base de datos ya existe")
            return

    def exist(self) -> bool:
        sql = "SHOW DATABASES"
        self.manager.execute(sql)
        for x in self.manager:
            if x == "client":
                return True
        return False

    def showDatabases(self):
        sql = "SHOW DATABASES"
        self.manager.execute(sql)
        for x in self.manager:
            print(x)

    def createTables(self):
        tb_pulso = '''CREATE TABLE pulso(
                pulso VARCHAR(10) NOT NULL,
                fecha DATETIME,
                id_doctor VARCHAR(10) NOT NULL,
                id_paciente VARCHAR(10) NOT NULL
        );
        '''

        tb_paciente = ''' CREATE TABLE paciente(
                id_paciente VARCHAR(10) NOT NULL,
                nombre VARCHAR(25) NOT NULL,
                edad INT NOT NULL,
                dpi VARCHAR(25) NOT NULL,
                peso FLOAT NOT NULL,
                altura FLOAT NOT NULL,
                id_doctor VARCHAR(10) NOT NULL
        );
        '''

        tb_doctor = ''' CREATE TABLE doctor(
                id_doctor VARCHAR(10) NOT NULL,
                nombre VARCHAR(25) NOT NULL,
                jornada VARCHAR(20) NOT NULL,
                clinica VARCHAR(20) NOT NULL
        )
        '''
        tables = [tb_pulso, tb_doctor, tb_paciente]
        for table in tables:
            self.manager.execute(table)

    def __del__(self):
        self.conn.close()

query_creator = Query("sql5.freesqldatabase.com", "sql5446566", "sql5446566", "HcIbUnlQtt")
query_creator.createDatabase()
query_creator.showDatabases()





