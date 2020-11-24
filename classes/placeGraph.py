from tkinter import * # NOQA
from matplotlib.figure import Figure # NOQA
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,# NOQA
                                               NavigationToolbar2Tk)
import csv
import pandas as pd
import matplotlib.animation as animation

class PlaceGraph():
    def __init__(self, root, c, fig, x, y1, canid, byte):
        data = pd.read_csv('dataFiles/dataCAN.csv')
        xvals = data['HOUR']
        yvals = data['MSG']
        yvals = [int(i.split('/')[byte]) for i in yvals]
  
        plot1 = fig.add_subplot(111)
        fig.set_facecolor("#2E3347")
        fig.tight_layout()
        plot1.patch.set_visible(False)
      
        plot1.plot(xvals, yvals, color='white')
        canvas = FigureCanvasTkAgg(fig, master=c)
        canvas.draw()
        canvas.get_tk_widget().place(x=root.winfo_screenwidth() *
                                     x, y=root.winfo_screenheight() * y1,anchor='center')

    def graph(i):
        data = pd.read_csv('dataFiles/dataCAN.csv')
        xvals = data['HOUR']
        yvals = data['MSG']
        yvals = [int(i.split('/')[byte]) for i in yvals]