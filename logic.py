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
import can

root = Tk()

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
xpng = ImageTk.PhotoImage(Image.open('rsc/data.png'))

