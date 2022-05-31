from tkinter import *
import time
from threading import *
  
# Create Object
root = Tk()
  
# Set geometry
root.geometry("400x400")
  
# use threading
  
continue_process = False 

def stop():
    # Call work function
    global continue_process
    continue_process = False
  
def start_process():
    global continue_process 
    continue_process = True
    t1 = Thread(target=work)
    t1.start()

# work function
def work():
    global continue_process
    print("sleep time start")
    i = 0
    while continue_process:
        print(i)
        time.sleep(1)
        i +=1
  
    print("sleep time stop")
  
# Create Button
Button(root,text="Start",command = start_process).pack()
Button(root, text="Stop", command = stop).pack()
  
# Execute Tkinter
root.mainloop()
