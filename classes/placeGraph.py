
from tkinter import * # NOQA
from matplotlib.figure import Figure # NOQA
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,# NOQA
                                               NavigationToolbar2Tk)
import csv
import pandas as pd



fig = Figure(figsize=(3,2))
fig.set_facecolor("#2E3347")
fig.set_tight_layout(True)


fig2 = Figure(figsize=(3,2))
fig2.set_facecolor("#2E3347")
fig2.set_tight_layout(True)

fig3 = Figure(figsize=(3,2))
fig3.set_facecolor("#2E3347")
fig3.set_tight_layout(True)


fig4 = Figure(figsize=(3,2))
fig4.set_facecolor("#2E3347")
fig4.set_tight_layout(True)
class PlaceGraph():
    def __init__(self, root, c, fig, x, y1, canid, byte,**kwargs):
        self.xtitle = kwargs.get('xtitle', '')
        self.ytitle = kwargs.get('ytitle', '')
        self.byte = byte
       
        self.plot1 = fig.add_subplot(111)
        self.plot1.set_facecolor("#2E3347")
        self.plot1.tick_params(axis='x', colors='white')
        self.plot1.tick_params(axis='y', colors='white')


        self.canvas = FigureCanvasTkAgg(fig, master=c)
        self.canvas.get_tk_widget().place(x=root.winfo_screenwidth() *
                                     x, y=root.winfo_screenheight() * y1,anchor='center')
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
       
        self.canvas.draw()
       