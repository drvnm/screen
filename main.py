from logic import *
import datetime
expression1 = """datetime.datetime.now().second % 2 == 0"""

#hier nieuwe plaatjes,tekst etc
baseImg = PlaceImage(root,'t.png',0.5,0.5,canvas,foto_x_resize=root.winfo_screenwidth(),foto_y_resize=root.winfo_screenheight())


moon = PlaceGif(root, canvas, 'e.gif',0.18,0.24,speed=200, resize='min',amount=6)

sunny = PlaceGif(root, canvas, 'sun.gif',0.18,0.24, resize='min',amount=3)

test = SwitchGifs(root,canvas,sunny,moon,expression1)

zonnenPanelenTekst = PlaceTxt(root,canvas,'Zonnenpanelen',0.218,0.365,size=17)

powerwallTekst = PlaceTxt(root,canvas,'Powerwall',0.718,0.333,size=17)

waterStofTekst = PlaceTxt(root,canvas,'Waterstof',0.7,0.72,size=17)

WarmteKoudopslag = PlaceTxt(root,canvas,'Warmte-Koudopslag',0.24,0.688,size=17)

waterboiler = PlaceTxt(root,canvas,'Waterboiler',0.5,0.26,size=17)
#hier komen alle grafieken
# graph = PlaceGraph(root,canvas,fig,0.2,0.2,24)


root.mainloop()
 