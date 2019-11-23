from tkinter import *
import tkinter.ttk as ttk


class Profile(ttk.Frame):
    def __init__(self, parent,beverage, **options):
        super().__init__(parent, **options)
        self.init_content(beverage)
        self.beverage = beverage

    def init_content(self, beverage):
        ttk.Style().configure('mainscreen.centerGrid.profile.TLabel', background="#871352", font="Helvetica 20",
                              foreground="white",justify="center", anchor="center")
        ttk.Style().configure('mainscreen.centerGrid.profile.small.TLabel', background="#871352", font="Helvetica 12",
                              foreground="white", justify="center", anchor="center")
        label = ttk.Label(self, text=beverage.name, style="mainscreen.centerGrid.profile.TLabel")
        label.grid(row=0, sticky="nsew", pady=(20, 10))
        ttk.Separator(self).grid(row=1, sticky="nsew",padx=(10, 25), pady=(20, 20))
        #label = Label(self, text=beverage.name)
        #label.grid(row=2)
        #ttk.Separator(self).grid(row=3, sticky="nsew", pady=(20, 10))
        label = ttk.Label(self, text=beverage.getingredients(), style="mainscreen.centerGrid.profile.small.TLabel", wraplength=130)
        label.grid(row=4, padx=(20, 20))

