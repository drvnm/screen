
from tkinter import * # NOQA
from matplotlib.figure import Figure # NOQA
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,# NOQA
                                               NavigationToolbar2Tk)
import csv
import pandas as pd



fig = Figure(figsize=(2,2))



class PlaceGraph():
    def __init__(self, root, c, x, y1, canid, byte):
        
        self.plot1 = fig.add_subplot(111)
        self.plot1.patch.set_visible(False)
        
        fig.set_facecolor("#2E3347")
        self.plot1.set_facecolor("#2E3347")
        fig.tight_layout()
       
        self.canvas = FigureCanvasTkAgg(fig, master=c)
        self.byte = byte
        self.canvas.get_tk_widget().place(x=root.winfo_screenwidth() *
                                     x, y=root.winfo_screenheight() * y1,anchor='center')
        
    def graph(self,i):
        data = pd.read_csv('dataFiles/data.csv')
        xvals = data['HOUR']
        yvals = data['MSG']
        yvals = [int(i.split('/')[self.byte]) for i in yvals]
        print(yvals)
        print('BYTE WAS:',self.byte)
        self.plot1.clear()
        print(yvals)
        self.plot1.plot(xvals, yvals, color='black')
        self.canvas.draw()
       