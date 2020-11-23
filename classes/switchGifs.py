from tkinter import *
import datetime

class SwitchGifs:
    def __init__(self,root, canvas, obj1, obj2, expression, **kwargs):
        self.obj1 = obj1
        self.obj2 = obj2
        self.root = root
        print(datetime.datetime.now().hour)
        self.canvas = canvas
        self.canid = kwargs.get('canid',None)
        self.bus = kwargs.get('bus',None)
        self.byte = kwargs.get('byte',None)
        self.max = kwargs.get('max',None)
        self.queue = bus.register(canid) if self.bus else None
        self.expression = expression 
        canvas.itemconfigure(self.obj1.canvasImg, state='hidden')
        canvas.itemconfigure(self.obj2.canvasImg, state='hidden')
        self.alternate()
    def alternate(self):
        if self.queue:
            msg = self.queue.get_nowait() # lees data
        if self.max:
            if msg.data[self.byte] < self.max // 2:
                self.speed = 120
            else:
                self.speed = 50
        if (eval(self.expression)):
            print(self.expression)
            self.canvas.itemconfigure(self.obj1.canvasImg, state='normal')
            self.canvas.itemconfigure(self.obj2.canvasImg, state='hidden')
        else:
            self.canvas.itemconfigure(self.obj2.canvasImg, state='normal')
            self.canvas.itemconfigure(self.obj1.canvasImg, state='hidden')
        self.root.after(500,self.alternate)
            
        
        

