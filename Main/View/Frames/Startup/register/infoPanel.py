import tkinter as tk
from tkinter import ttk

class InfoPanel(ttk.Frame):
    def __init__(self, parent, **options):
        super().__init__(parent, **options)
        self.init_content()

    def init_content(self):
        s = ttk.Style()
        s.configure('register.right.big.TLabel', font="Helvetica 15", foreground="white", background="#201F1E", padding=[0,0,0,10], justify="center", anchor="center")
        s.configure('register.right.small.TLabel', font="Helvetica 10", foreground="white", background="#201F1E",padding=5, justify="left", anchor="center")
        ttk.Label(self, text="Website: barman.at", style="register.right.big.TLabel").grid(row=0, sticky="we")
        ttk.Label(self, text="Key: ", style="register.right.big.TLabel").grid(row=1, sticky="we")
        ttk.Label(self, text="PWD: ", style="register.right.big.TLabel").grid(row=2, sticky="we")
        ttk.Button(self, text="Refresh", padding=[100,5]).grid(row=3)
        ttk.Separator(self).grid(row=4, sticky="we")
        ttk.Label(self, width=50, style="register.right.small.TLabel", text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy\n eirmod tempor invidunt ut labore et dolore magna aliquyam erat\n sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,\n no sea takimata sanctus est Lorem ipsum dolor sit amet.").grid(row=5,sticky="we")


