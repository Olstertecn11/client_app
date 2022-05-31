from tkinter import *
import time
from threading import *
  
root = Tk()
root.geometry("400x400")
  
  


class _Interface(object):

    def __init__(self, master):
        self.frame = master
        self.continue_process = False
        self.createButtons()

    def stop(self):
        # Call work function
        self.continue_process = False
  
    def start_process(self):
        self.continue_process = True
        t1 = Thread(target=self.work)
        t1.start()

    def work(self):
        print("sleep time start")
        i = 0
        while self.continue_process:
            print(i)
            time.sleep(1)
            i +=1
      
        print("sleep time stop")
      
    def createButtons(self):
        Button(self.frame,text="Start",command = self.start_process).pack()
        Button(self.frame, text="Stop", command = self.stop).pack()
  
application = _Interface(root)
root.mainloop()
