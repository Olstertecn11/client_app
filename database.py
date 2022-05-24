from connection_controller import Connection 
from database_controller import DatabaseController 
from templates.pulso import Pulso
from templates.paciente import Paciente
from templates.doctor import Doctor 
from views import _print, _print_doctor



class Database:
    
    def __init__(self):
        self.connection_obj = Connection(
                host="sql5.freesqldatabase.com", 
                user="sql5494968",
                password="HXKCRiWBq6",
                db="sql5494968")

        self.cursor = self.connection_obj.get_cursor()
        self.connection = self.connection_obj.get_connection()
        self.connection_obj.isConnected()

    def add_pulso(self, pulso: Pulso):
        pulso_obj = DatabaseController()
        query = "insert into tb_pulso (pulso, fecha, id_doctor, id_paciente) values ('{}', '{}', '{}', '{}')"
        query = query.format(pulso.pulso, pulso.fecha, pulso.id_doctor, pulso.id_paciente)
        pulso_obj._add(self.connection,self.cursor,query)

    def add_paciente(self, paciente: Paciente):
        controller_obj = DatabaseController()
        query = """insert into tb_paciente (id_paciente, nombre, edad, dpi, peso, altura, id_doctor) 
                values ('{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
        query = query.format(paciente._id, 
                paciente.nombre, 
                paciente.edad, 
                paciente.dpi, 
                paciente.peso, 
                paciente.altura, 
                paciente.id_doctor)

        controller_obj._add(self.connection,self.cursor,query)


    def add_doctor(self, doctor: Doctor):
        controller_obj = DatabaseController()
        query = """insert into tb_doctor (id_doctor, nombre, jornada, clinica) 
                values ('{}', '{}', '{}', '{}')"""
        query = query.format(doctor._id, doctor.name, doctor.working_day, doctor.clinic)
        controller_obj._add(self.connection,self.cursor,query)

    def get_pulso(self):
        controller_obj = DatabaseController()
        query = "select * from tb_pulso"
        return controller_obj._get(self.connection,self.cursor,query)
    
    def get_paciente(self):
        controller_obj = DatabaseController()
        query = "select * from tb_paciente"
        return controller_obj._get(self.connection,self.cursor,query)
    
    def get_doctor(self):
        controller_obj = DatabaseController()
        query = "select * from tb_doctor"
        return controller_obj._get(self.connection,self.cursor,query)




    


database_manager = Database()
# d_simmi = Doctor(2, "Luis", "Sabado", "San Marcelo")
# database_manager.add_doctor(d_simmi)
# doctores = database_manager.get_doctor()
# _print_doctor(doctores)
p_oliver = Paciente(1, "Oliver", "25", "123456789", "70", "1.70", 1)
# database_manager.add_paciente(p_oliver)
pacientes = database_manager.get_paciente()
_print(pacientes)










