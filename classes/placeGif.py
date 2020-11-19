from tkinter import * # NOQA
from PIL import Image, ImageTk # NOQA


class PlaceGif():
    def __init__(self, root, canvas, filename, x, y, **kwargs):
        self.speed = 50
        self.frameCount = Image.open("rsc/" + filename).n_frames
        if 'resize' in kwargs and 'amount' in kwargs:
            if kwargs['resize'] == 'min':
                self.frames = [PhotoImage(file='rsc/' + filename ,format = 'gif -index %i' %(i)).subsample(kwargs['amount']) for i in range(self.frameCount)]
            elif kwargs['resize'] == 'max':
                self.frames = [PhotoImage(file='rsc/' + filename ,format = 'gif -index %i' %(i)).zoom(kwargs['amount']) for i in range(self.frameCount)]
        else:     
            self.frames = [PhotoImage(file='rsc/' + filename ,format = 'gif -index %i' %(i)) for i in range(self.frameCount)]
        tkinterImg = PhotoImage(file='rsc/' + filename) 
        self.canvasImg = canvas.create_image(root.winfo_screenwidth() * x, root.winfo_screenheight() * y, image=tkinterImg, anchor='center')

        self.index = 0
        self.animateGif(canvas, root)    

    def changeSpeed(self, speed):
        self.speed = speed

    def animateGif(self, canvas, root):
        frame = self.frames[self.index]

        self.index += 1
        if self.index == self.frameCount - 2:
            self.index = 0

        canvas.itemconfig(self.canvasImg, image=frame)
        root.after(self.speed, self.animateGif, canvas, root)