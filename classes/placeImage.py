from tkinter import * # NOQA
from PIL  import Image, ImageTk # NOQA


class PlaceImage():
    def __init__(self, root, img, fotox, fotoy, canvas, **kwargs):
        """ Deze class zorgt ervoor dat je gemakkelijk een foto op het scherm kan plaatsen
        Arguments : 
            root ([object]) : de root widget, dit zal altijd root zijn
            img (string) : de locatie van de foto die je in de GUI wilt plaatsen
            fotox (float) : x coördinaat voor de foto (als je hem in het midden wilt moet je 0.5 invoeren)
            fotoy (float) : y coördinaat voor de foto (als je hem in het midden wilt moet je 0.5 invoeren)

        Keyword arguments (kwargs):
            foto_x_resize (integer): hoe breed de foto moet worden (optioneel)
            foto_y_resize (integer): hoe hoog de foto moet worden (optioneel)
            anchor (string): anchor voor de foto (optioneel)
        """
        self.root = root
        # Hier word gekeken of er aan gegeven is of je de foto wilt resizen
        # Als dit het geval is MOET je beide foto_x_resize en foto_y_resize invullen anders zal het programma het negeren
        if 'foto_x_resize' in kwargs and 'foto_y_resize' in kwargs:
            self.png = ImageTk.PhotoImage(Image.open('rsc/' + img).resize((kwargs['foto_x_resize'], kwargs['foto_y_resize']), Image.ANTIALIAS))
        else:
            self.png = ImageTk.PhotoImage(Image.open('rsc/' + img))
        # hier word de foto geplaatst
        self.image = canvas.create_image(root.winfo_screenwidth() * fotox, root.winfo_screenheight() * fotoy, image=self.png, anchor=kwargs['anchor'] if 'anchor' in kwargs else 'center')
