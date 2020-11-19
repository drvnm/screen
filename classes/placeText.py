from tkinter import * # NOQA


class PlaceTxt():
    def __init__(self, root, canvas, txt, txtx, txty, **kwargs):                    
        self.root = root                                                       
        self.text = canvas.create_text(root.winfo_screenwidth() * txtx, root.winfo_screenheight() * txty, text=txt, fill=kwargs['kleur'] if 'kleur' in kwargs else 'white',
                                                                        font=(kwargs['font'] if 'font' in kwargs else "Times 10",
                                                                            kwargs['size'] if 'size' in kwargs else 20))
