from tkinter import *
import datetime

class SwitchGifs:
    def __init__(self,root, canvas,bus, canid, byte, obj1, obj2, expression):
        self.obj1 = obj1
        self.obj2 = obj2
        self.root = root
        print(datetime.datetime.now().hour)
        self.canvas = canvas
        self.expression = expression 
        canvas.itemconfigure(self.obj1.canvasImg, state='hidden')
        canvas.itemconfigure(self.obj2.canvasImg, state='hidden')
        self.alternate()
    def alternate(self):
        if (eval(self.expression)):
            print(self.expression)
            self.canvas.itemconfigure(self.obj1.canvasImg, state='normal')
            self.canvas.itemconfigure(self.obj2.canvasImg, state='hidden')
        else:
            self.canvas.itemconfigure(self.obj2.canvasImg, state='normal')
            self.canvas.itemconfigure(self.obj1.canvasImg, state='hidden')
        self.root.after(500,self.alternate)
            
        
        

