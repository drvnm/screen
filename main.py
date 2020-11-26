from logic import *
import datetime
expression1 = """datetime.datetime.now().hour < 17"""

#hier nieuwe plaatjes,tekst etc
baseImg = PlaceImage(root,'h.png',0.52,0.52,canvas,foto_x_resize=root.winfo_screenwidth()-390,foto_y_resize=root.winfo_screenheight())


# moon = PlaceGif(root, canvas, 'e.gif',0.18,0.24,speed=200, resize='min',amount=6)
windmolen = PlaceGif(root, canvas, 'fw.gif',0.25,0.42,speed=50)
# sunny = PlaceGif(root, canvas, 'SUN2.gif',0.18,0.24, resize='min',amount=3,speed=100)
 
# test = SwitchGifs(root,canvas, sunny,moon,expression1)

zonnenPanelenTekst = PlaceTxt(root,canvas,'Zonnepanelen',0.57,0.264,size=17)

powerwallTekst = PlaceTxt(root,canvas,'Powerwall',0.658,0.413,size=17) 

waterStofTekst = PlaceTxt(root,canvas,'Waterstof',0.778,0.643,size=17)

warmteKoudopslag = PlaceTxt(root,canvas,'Warmte-Koudopslag',0.27,0.743,size=17)

waterboiler = PlaceTxt(root,canvas,'Waterboiler',0.52,0.17,size=17)
windmolen = PlaceTxt(root,canvas,'Windmolen',0.169,0.554,size=17)
#hier komen alle grafieken
 
# graph = PlaceGraph(root,canvas,0.77,0.85,0x100400,0) 
# ani2 = animation.FuncAnimation(fig,graph.graph,interval=1000)

graph1 = PlaceGraph(root,canvas,fig,0.8,0.24,0x100400,2,xtitle='Uren',ytitle='Waarden') 
ani2 = animation.FuncAnimation(fig,graph1.graph,interval=2000)

graph2 = PlaceGraph(root,canvas, fig2, 0.13,0.12,0x100400,4,xtitle='Uren',ytitle='Waarden') 
ani3 = animation.FuncAnimation(fig2,graph2.graph,interval=2000)

graph3 = PlaceGraph(root,canvas, fig3, 0.53,0.52,0x100400,0,xtitle='Uren',ytitle='g') 
ani4 = animation.FuncAnimation(fig3,graph3.graph,interval=2000)

graph4 = PlaceGraph(root,canvas, fig4, 0.83,0.82,0x100400,1,xtitle='Uren',ytitle='E') 
ani5 = animation.FuncAnimation(fig4,graph4.graph,interval=2000)

bus.start()
root.mainloop()
