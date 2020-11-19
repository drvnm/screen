from tkinter import *

class PlaceInfo():
    def __init__(self, bus, root, textx, texty, canid, byte, **kwargs):  
        self.root = root  
     
        # hier word voor 2 variable gekeken of ze zijn aangegeven
        # als dit niet het geval is word er een standaard waarde aan gegeven
        fill = kwargs.get('kleur', 'white')
        size = kwargs.get('size', 10)         
        #hier wordt er text gemaakt op basis van de argumenten die je aangeeft
        self.text = canvas.create_text(textx*800, texty*480, text='???', fill=fill, font=('arial',size))                
        self.queue = bus.register(canid) # register aan de CanReader met canid
        #hier call ik een functie die de data op het scherm zal veranderen
        self.changeData(canid, byte,kwargs['postfix'] if 'postfix' in kwargs else '', kwargs['som'] if 'som' in kwargs else None)

    #method voor het updaten van het scherm
    def changeData(self, canid, byte, postfix,som):
        try:
            somholder = som
            msg = self.queue.get_nowait() # lees data

            # hier word gekeken of een som is aan gegeven
            # als dit het geval is word deze gebruikt om de eind waarde te laten zien, als dat niet zo is wordt het niet gebruikt
            if som == None:
                self.data = msg.data[byte]
                canvas.itemconfigure(self.text, text=str(self.data) + postfix) #verander text op scherm
            else:
                self.data = msg.data[byte]
                newSom = somholder.replace('byte',str(self.data)) #verander 'byte' met de data die aan komt
                result = eval(newSom) #berekent de som
                canvas.itemconfigure(self.text, text=str(result) + postfix) #verander text op scherm
        except Exception as e:
            pass
            
        self.root.after(40, self.changeData, canid, byte,postfix,som) #herhaal dit elke 40 milliseconden