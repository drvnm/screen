from tkinter import *
from classes.placeImage import PlaceImage
from classes.placeGif import PlaceGif
from classes.placeText import PlaceTxt
from classes.placeGraph import *
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
import pandas as pd
from classes.canReader import CanReader
from classes.placeCanText import PlaceInfo
import matplotlib.animation as animation

from matplotlib.widgets import Button as GraphButton

from classes.switchGifs import SwitchGifs


plt.rcParams['toolbar'] = 'None'
root = Tk()
plt.rcParams['axes.grid'] = True


def graph(i):
    data = pd.read_csv('dataFiles/data.csv')
    x = data['HOUR']
    y = data['MSG']
    holder = [i.split('/') for i in y]
    ynew = [i[0] for i in holder]
    ynew = [int(i) for i in ynew]
    # print(ax1,ax2,ax3,ax4)

    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()

    ax1.plot(x, ynew, linewidth=2)
    ax1.set_title('windmolen')

    ax2.plot(x, ynew, linewidth=2)
    ax2.set_title('batterij')

    ax3.plot(x, ynew, linewidth=2)
    ax3.set_title('windmolen')
    
    ax4.plot(x, ynew, linewidth=2)
    ax4.set_title('e3')
    
    axButton = plt.axes([0.465, 0.9, 0.1, 0.075])
    bMainScreen = GraphButton(axButton, 'Main Screen')
    bMainScreen.on_clicked(callback.mainScreen)


def mainScreen():
    plt.close()

def Graph():
    global ax1,ax2,ax3,ax4
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
    fig.patch.set_facecolor('#4d577d')
    ax1.set_facecolor('#AAAABB')
    ax2.set_facecolor('#AAAABB')
    ax3.set_facecolor('#AAAABB')
    ax4.set_facecolor('#AAAABB')
    ani = animation.FuncAnimation(fig,graph,interval=1000)
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.show()

    # ani = FuncAnimation(plt.gcf(), graph, interval=1000)
# ===== niet veranderen

bus = CanReader('can0')
root.geometry("1920x1080")
root.bind('<Escape>', quit)
SCREENWIDTH = root.winfo_screenwidth()
SCREENHEIGHT = root.winfo_screenheight()


def quit(event):
    root.quit()


root.attributes("-fullscreen", True)
canvas = Canvas(root, height=1080, width=1920,
                highlightthickness=0, background='#2E3347')
canvas.pack(fill="both", expand=True)
fig = Figure(figsize=(1,1))

xpng = ImageTk.PhotoImage(Image.open('rsc/data.png'))
graphButton = Button(canvas,image=xpng, command=Graph, borderwidth=0, bd=0, highlightthickness=0)
graphButton.place(x=SCREENWIDTH - 191.5, y=0)
