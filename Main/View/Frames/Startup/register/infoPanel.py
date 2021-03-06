from tkinter import *
from tkinter import ttk

class InfoPanel(ttk.Frame):
    def __init__(self, key, pin, parent, **options):
        super().__init__(parent, **options)
        self.key = key
        self.pin = pin
        s = ttk.Style()
        s.configure('register.right.big.TLabel', font="Helvetica 15", foreground="white", background="#201F1E", padding=[0,0,0,10], justify="center", anchor="center")
        s.configure('register.right.small.TLabel', font="Helvetica 10", foreground="white", background="#201F1E",padding=5, justify="center", anchor="center", wraplength=360)
        s.configure('register.right.TFrame', background="#201F1E",)
        data = ttk.Frame(self, padding=[0,100,0,0],style="register.right.TFrame")
        Grid.rowconfigure(self, 0, weight=1)
        Grid.rowconfigure(self, 1, weight=1)
        Grid.rowconfigure(self, 2, weight=1)
        ttk.Label(data, text="Website: f-parfuss.at/barman/app", style="register.right.big.TLabel").grid(row=0, sticky="nsew")
        ttk.Label(data, text="Key: "+str(self.key), style="register.right.big.TLabel").grid(row=1, sticky="nsew")
        ttk.Label(data, text="Pin: "+str(self.pin), style="register.right.big.TLabel").grid(row=2, sticky="nsew")
        data.pack(side=TOP)
        info = Frame(self)
        info.pack(side=BOTTOM)
        ttk.Separator(info).grid(row=4,sticky="nsew")
        label = ttk.Label(info, style="register.right.small.TLabel", text="Scannen Sie den QR-Code oder geben Sie den Link in Ihnrem Browser ein! Sobald sie die Änderungen vorgenommen haben, sollte der BarMan automatisch die Verbindung erkennen")
        label.grid(row=5,sticky="nsew")


