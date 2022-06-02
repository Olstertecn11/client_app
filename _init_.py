from tkinter import *
from tkinter import ttk 
from database import Database
from master import _run_


class _App:

    def __init__(self, master):
        self.frame = master 
        self.controller = Database()
        self.paciente = StringVar()
        self.createBox()
        self.fillPacientes()
        self.drawButtons()

    def fillPacientes(self):
        self.pacientes = self.controller.get_paciente()
        elementos = []
        for i in self.pacientes:
            elementos.append(i[1])
        docs = []
        ds = self.controller.get_doctor()
        for i in ds:
            docs.append(i[1])
        self.list_pacientes['values'] = elementos
        self.list_doctores['values'] = docs





    def createBox(self):
        self.list_pacientes = ttk.Combobox(self.frame)
        self.list_pacientes.place(x = 20, y = 80)
        self.label_pa = Label(self.frame, font=('Arial', 14),fg="white",text="Paciente",bg="#303030").place(x=20, y=40)

        self.list_doctores = ttk.Combobox(self.frame)
        self.list_doctores.place(x = 200, y = 80)
        self.label_doc = Label(self.frame , font=('Arial', 14), fg="white", text="Doctor",bg="#303030").place(x=200, y=40)

    def ejecutar(self):
        paciente = self.list_pacientes.get()
        doctor = self.list_doctores.get()
        obj_paciente = None 
        print(doctor)
        for i in self.pacientes:
            if i[1] == paciente:
                obj_paciente = i 
        _run_(obj_paciente)


    def drawButtons(self):
        self.btn = Button(self.frame, relief="flat",bg="#249862",fg="white",text="Continuar", command=lambda:self.ejecutar()).place(x = 120, y=150, width=150)





root = Tk()
root.title("Iniciando")
root.geometry("400x250")
root.configure(bg="#303030")
initial_app = _App(root)
root.mainloop()
