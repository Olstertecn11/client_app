import threading
from tkinter import *
import tkinter as tk
import serial
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = tk.Tk()
COM = "/dev/ttyUSB0"
ser = serial.Serial(port=COM, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=2)
ser.isOpen()
msg = "jfksadk"


# read Serial
def ReadSerial():
    global msg
    msg = ""
    msg = ser.readline()[:-2].decode("utf-8")
    if msg != "":

        print(msg)
        
    return msg
# write Serial
def WriteSerial(sendmsg):
    print("send")
    ser.write(bytes(sendmsg, 'utf-8'))
    ReadSerial()


# Tkinter
root.title("WIP NAME")
root.geometry("650x400")
inputData = Entry(root, text="<Slave1&p>") # input for enter the message to write
entrymsg = inputData.get() # get the massage
buttonMsg = Button(root, text="send", command = lambda: WriteSerial(inputData.get())) # create a send button for send the message
textLabel = StringVar()
readData = Label(root, textvariable=textLabel) # show message in Tkinter
ReadSerial()
# show items
inputData.grid()
readData.grid()
buttonMsg.grid()


def createGra():
    data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
         'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
        }
    df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])
    figure2 = plt.Figure(figsize=(5,4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
    ax2.set_title('Year Vs. Unemployment Rate') 


# GUI thread
def TkinterGui():
    while 1==1:
        global msg
        msg = inputData.get()


# Serial thread
def SerialProgram():
    while 1==1:
        ReadSerial()
        print("SerialProgram")
        textLabel.set(msg)




x = threading.Thread(target=TkinterGui, args=())
y = threading.Thread(target=SerialProgram, args=())
x.start()
y.start()

root.mainloop()
