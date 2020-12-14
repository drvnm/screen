
from tkinter import *  # NOQA
import matplotlib.dates as md

from matplotlib.figure import Figure  # NOQA
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  # NOQA
                                               NavigationToolbar2Tk)
from matplotlib import dates as mpl_dates
import datetime
import random

fig = Figure(figsize=(4, 2))
fig.set_facecolor("#2E3347")
fig.set_tight_layout(True)


fig2 = Figure(figsize=(4, 2))
fig2.set_facecolor("#2E3347")
fig2.set_tight_layout(True)

fig3 = Figure(figsize=(4, 2))
fig3.set_facecolor("#2E3347")
fig3.set_tight_layout(True)


fig4 = Figure(figsize=(4, 2))
fig4.set_facecolor("#2E3347")
fig4.set_tight_layout(True)


class PlaceGraph():
    def __init__(self, root, c, fig, bus, x, y1, canid, byte, **kwargs):
        self.xtitle = kwargs.get('xtitle', '')
        self.ytitle = kwargs.get('ytitle', '')
        self.title = kwargs.get('title', '')
        self.byte = byte
        self.yvals = []
        self.xvals = []
        self.plot1 = fig.add_subplot(111)
        self.plot1.set_facecolor("#2E3347")
        self.plot1.tick_params(axis='x', colors='white')
        self.plot1.tick_params(axis='y', colors='white')
     
        self.canvas = FigureCanvasTkAgg(fig, master=c)
        self.canvas.get_tk_widget().place(x=root.winfo_screenwidth() *
                                          x, y=root.winfo_screenheight() * y1, anchor='center')
        
        self.plot1.xaxis.label.set_color('white')
        self.plot1.yaxis.label.set_color('white')
        # self.queue = bus.register(canid)
    
        
    def graph(self, i):
        try:
           
            if len(self.yvals) >= 23:
                self.yvals.pop(0)
                self.xvals.pop(0)
            
            #msg = self.queue.get_nowait() # lees data
            #print('MSG : ' + str(msg.data[self.byte]))
            datetimeobject = datetime.datetime.now()
           
            #self.yvals.append(msg.data[self.byte])
            self.yvals.append(random.randint(0, 255))
            self.xvals.append(datetimeobject)
         
            self.plot1.clear()
            print(self.yvals)

            
            date_format = mpl_dates.DateFormatter('%S')
            self.plot1.xaxis.set_major_formatter(date_format)
            self.plot1.plot_date(self.xvals, self.yvals, color='white',linestyle='solid')
            self.plot1.set_xlabel(self.xtitle)
            self.plot1.set_ylabel(self.ytitle)
            self.plot1.set_title(self.title, color='white')
            self.canvas.draw()
        except Exception as e:
            print(e)
            pass
