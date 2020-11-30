from logic import *
import datetime
expression1 = """datetime.datetime.now().hour < 17"""

#hier nieuwe plaatjes,tekst etc
baseImg = PlaceImage(root,'h.png',0.52,0.52,canvas,foto_x_resize=root.winfo_screenwidth()-390,foto_y_resize=root.winfo_screenheight())


# moon = PlaceGif(root, canvas, 'e.gif',0.18,0.24,speed=200, resize='min',amount=6)
windmolen = PlaceGif(root, canvas, 'fw.gif',0.25,0.42,speed=50)
sung = PlaceGif(root, canvas, 'sun.gif',0.38,0.138,speed=50,resize='min',amount=4)


zonnenPanelenTekst = PlaceTxt(root,canvas,'Zonnepanelen',0.57,0.264,size=17)

powerwallTekst = PlaceTxt(root,canvas,'Powerwall',0.658,0.413,size=17) 

waterStofTekst = PlaceTxt(root,canvas,'Waterstof',0.778,0.643,size=17)

warmteKoudopslag = PlaceTxt(root,canvas,'Warmte-Koudopslag',0.27,0.743,size=17)

waterboiler = PlaceTxt(root,canvas,'Waterboiler',0.52,0.17,size=17)
windmolen = PlaceTxt(root,canvas,'Windmolen',0.169,0.554,size=17)
#hier komen alle grafieken
 
# graph = PlaceGraph(root,canvas,0.77,0.85,0x100400,0) 
# ani2 = animation.FuncAnimation(fig,graph.graph,interval=1000)

# graph1 = PlaceGraph(root,canvas,fig, bus, 0.8,0.24,0x1000400,2,xtitle='Uren',ytitle='TEST!!!!') 
# ani2 = animation.FuncAnimation(fig,graph1.graph,interval=1000)

# graph2 = PlaceGraph(root,canvas, fig2,bus, 0.13,0.12,0x1000400,4,xtitle='Uren',ytitle='TEST') 
# ani3 = animation.FuncAnimation(fig2,graph2.graph,interval=2000)

# graph3 = PlaceGraph(root,canvas, fig3,bus, 0.83,0.8,0x1000400,0,xtitle='Uren',ytitle='g') 
# ani4 = animation.FuncAnimation(fig3,graph3.graph,interval=2000)

graph4 = PlaceGraph(root,canvas, fig4,bus, 0.1,0.87,0x1000400,1,xtitle='Uren',ytitle='E') 
ani5 = animation.FuncAnimation(fig4,graph4.graph,interval=20)

bus.start()
root.mainloop()
