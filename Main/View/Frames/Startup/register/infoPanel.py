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
        ttk.Label(self, text="Website: barman.at", style="register.right.big.TLabel").grid(row=0)
        ttk.Label(self, text="Key: "+str(self.key), style="register.right.big.TLabel").grid(row=1, sticky="we")
        ttk.Label(self, text="PWD: "+str(self.pin), style="register.right.big.TLabel").grid(row=2, sticky="we")
        self.refresh = ttk.Button(self, text="Refresh", padding=[100,5])
        self.refresh.grid(row=3)
        ttk.Separator(self).grid(row=4,sticky="nsew", pady=(20,10))
        label = ttk.Label(self, style="register.right.small.TLabel", text="Scannen Sie den QR-Code oder geben Sie den Link in Ihnrem Browser ein")
        label.grid(row=5,sticky="nsew")


