from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk



class Pumpsscreen(ttk.Frame):
    def __init__(self, parent, pumps, callback, **options):
        super().__init__(parent, **options)
        Grid.columnconfigure(self, 0, weight=1)
        Grid.rowconfigure(self, 1, weight=1)
        ttk.Style().configure('pumpscreen.topframe.TFrame', background="#87014F")
        ttk.Style().configure('pumpscreen.bottomFrame.TFrame', background="#201F1E")

        TopFrame(self,callback, padding=[20,10,0,10] ,style="pumpscreen.topframe.TFrame").grid(row=0,sticky="nsew")
        BottomFrame(self,pumps, style="pumpscreen.bottomFrame.TFrame").grid(row=1,sticky="nsew")

class TopFrame(ttk.Frame):
    def __init__(self, parent, callback, **options):
        super().__init__(parent, **options)
        ttk.Style().configure('pumps.topframe.TLabel', background="#87014F", font="Helvetica 18", foreground="white")
        logo = Image.open("images/chevron-left-solid.png")
        logo = logo.resize((17, 25), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)
        button = Label(self, background="#87014F", image=logo)
        button.photo = logo
        button.pack(side="left")

class BottomFrame(ttk.Frame):
    def __init__(self, parent, pumps, **options):
        super().__init__(parent, **options)
        Grid.columnconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 1, weight=1)
        Grid.columnconfigure(self, 2, weight=1)
        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,0,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        ttk.Style().configure('pumps.bottomFrame.TLabel', justify="center", background="#201F1E", font="Helvetica 20", foreground="white")
        for pump in pumps:
            if pump.containerid % 2 == 0:
                label = ttk.Label(self, style="pumps.bottomFrame.TLabel", text=pump.name).grid(sticky="nsew", row=int((pump.containerid / 2) % 2),
                                                             column=0)
            else:
                label = ttk.Label(self, style="pumps.bottomFrame.TLabel", text=pump.name).grid(sticky="nsew", row=int((pump.containerid / 2) % 2),
                                                             column=2)

        logo = Image.open("images/tint-solid.png")
        logo = logo.resize((250, 250), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)
        button = Label(self, background="#87014F", image=logo)
        button.photo = logo
        button.grid(row=0, column=1, rowspan=2, padx=(10, 10))
