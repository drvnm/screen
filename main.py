from logic import *
import datetime
expression1 = """datetime.datetime.now().hour < 17"""

#hier nieuwe plaatjes,tekst etc
baseImg = PlaceImage(root,'h.png',0.5,0.5,canvas,foto_x_resize=root.winfo_screenwidth()-390,foto_y_resize=root.winfo_screenheight())


# moon = PlaceGif(root, canvas, 'e.gif',0.18,0.24,speed=200, resize='min',amount=6)
windmolen = PlaceGif(root, canvas, 'w.gif',0.24,0.3,speed=50)

# sunny = PlaceGif(root, canvas, 'test.gif',0.18,0.24, resize='min',amount=3)
 
# test = SwitchGifs(root,canvas, sunny,moon,expression1)

zonnenPanelenTekst = PlaceTxt(root,canvas,'Zonnepanelen',0.55,0.244,size=17)

powerwallTekst = PlaceTxt(root,canvas,'Powerwall',0.638,0.393,size=17) 

waterStofTekst = PlaceTxt(root,canvas,'Waterstof',0.758,0.623,size=17)

WarmteKoudopslag = PlaceTxt(root,canvas,'Warmte-Koudopslag',0.24,0.723,size=17)

waterboiler = PlaceTxt(root,canvas,'Waterboiler',0.49,0.12,size=17)
#hier komen alle grafieken

# graph = PlaceGraph(root,canvas,0.77,0.85,0x100400,0) 
# ani2 = animation.FuncAnimation(fig,graph.graph,interval=1000)

graph1 = PlaceGraph(root,canvas,0.82,0.2,0x100400,2,xtitle='Uren',ytitle='Waarden') 
ani3 = animation.FuncAnimation(fig,graph1.graph,interval=10000)
bus.start()
root.mainloop()
