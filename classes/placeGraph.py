from tkinter import * # NOQA
from matplotlib.figure import Figure # NOQA
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,# NOQA
                                               NavigationToolbar2Tk)


class PlaceGraph():
    def __init__(self, root, c, fig, x: int, y1: str, maxVal: int) -> None:
        y = [i for i in range(maxVal + 1)] 
  
        plot1 = fig.add_subplot(111)
        fig.set_facecolor("#2E3347")

        plot1.patch.set_visible(False)
       
        plot1.plot(y, color='white')
        canvas = FigureCanvasTkAgg(fig, master=c)
        canvas.draw()
        canvas.get_tk_widget().place(x=root.winfo_screenwidth() *
                                     x, y=root.winfo_screenheight() * y1)
