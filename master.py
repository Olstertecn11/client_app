from tkinter import *
import time
from threading import *
import socket
  
root = Tk()
root.geometry("400x300")
  
  


class _Interface(object):

    def __init__(self, master):
        self.frame = master
        self.continue_process = False
        self.title = StringVar()
        self.title.set("click en `Start` :D")
        self.createButtons()
        self._socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self._socket.connect(('00:21:07:00:55:5F', 1))
        self._socket.send(b"0")



    def stop(self):
        # Call work function
        self.title.set("Proceso Finalzado")
        self.continue_process = False
        self._socket.close()
  
    def start_process(self):
        self.title.set("Leyendo datos")
        self.continue_process = True
        t1 = Thread(target=self.work)
        t1.start()

    def work(self):
        print("sleep time start")
        while self.continue_process:
            data = self._socket.recv(1024)
            print(data)
            time.sleep(1)
      
        print("sleep time stop")
      
    def createButtons(self):
        self.label = Label(self.frame,fg="white",font=("Arial", 16),bg="#303030" ,textvariable=self.title).place(x = 100, y = 60)
        Button(self.frame,text="Start", relief="flat",bg="#249862",font=("Arial", 12), fg="white",command = self.start_process).place(x=70, y = 150, width=100)
        Button(self.frame, text="Stop" ,relief="flat", bg="#DF0025",font=("Arial", 12), fg="white",command = self.stop).place(x= 220, y = 150, width=100)
  


root.title("Capturador de Datos")
root.configure(bg="#303030")
application = _Interface(root)
root.mainloop()
