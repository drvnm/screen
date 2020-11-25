
from tkinter import * # NOQA
from matplotlib.figure import Figure # NOQA
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,# NOQA
                                               NavigationToolbar2Tk)
import csv
import pandas as pd



fig = Figure(figsize=(3,2))



class PlaceGraph():
    def __init__(self, root, c, x, y1, canid, byte,**kwargs):
        
        self.plot1 = fig.add_subplot(111)
        self.plot1.patch.set_visible(False)
        
        fig.set_facecolor("#2E3347")
        self.plot1.set_facecolor("#2E3347")
        fig.tight_layout()
        self.plot1.tick_params(axis='x', colors='white')
        self.plot1.tick_params(axis='y', colors='white')
        self.canvas = FigureCanvasTkAgg(fig, master=c)
        self.byte = byte
        self.canvas.get_tk_widget().place(x=root.winfo_screenwidth() *
                                     x, y=root.winfo_screenheight() * y1,anchor='center')
        xtitle = kwargs.get('xtitle', '')
        ytitle = kwargs.get('ytitle', '')
        self.xtitle = xtitle
        self.ytitle = ytitle
        self.plot1.xaxis.label.set_color('white')
        self.plot1.yaxis.label.set_color('white')
        
    def graph(self,i):
        data = pd.read_csv('dataFiles/data.csv')
        xvals = data['HOUR']
        yvals = data['MSG']
        yvals = [int(i.split('/')[self.byte]) for i in yvals]
        print(yvals)
        print('BYTE WAS:',self.byte)
        self.plot1.clear()
        print(yvals)
        self.plot1.plot(xvals, yvals, color='white')
        self.plot1.set_xlabel(self.xtitle)
        self.plot1.set_ylabel(self.ytitle)
        fig.tight_layout()
        self.canvas.draw()
       