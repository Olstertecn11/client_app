import pymysql


#host, user, database, password
connector = pymysql.connect(host="sql3.freesqldatabase.com", 
        user="sql3491857", 
        database="sql3491857", 
        password="j7hMsSZEWC")

if connector:
    print("Conexion realizada!")
    sql = "insert into doctor(id_doctor, nombre, jornada, clinica) values ('{}', '{}', '{}', '{}')".format("004", 
    "Oliver", 
    "Matutina",
    "El Sol")
    cursor = connector.cursor()
    cursor.execute(sql)
    connector.commit()
else:
    print("Error")




